from typing import get_type_hints
from log import log
from enum import Enum
import os.path

supported_register_types = ["w", "x", "b", "h", "s", "d", "q"]

class asm_inst:
  def __init__(self, function="", address="", hexValue = "", instruction="", params = []):
    self.function = function
    self.address = address
    self.hexValue = hexValue
    self.instruction = instruction
    self.params = params

class ptype_type(Enum):
    """Parameter Types

    :param Enum: ENUM ONLY (do not use)
    :type Enum: NOT
    """
    sys_init = "SYS_INIT"
    pointer = "POINTER"
    number = "NUMBER"
    register = "REGISTER"
    address = "ADDRESS"
    unkown = "UNKNOWN"

class ftype_type(Enum):
    
    sys_init = "SYS_INIT"
    input = "INPUT"
    output = "OUTPUT"
    general_purpose = "GP"

class dtype_type(Enum):
    i32 = "i32"     #W-Registers
    i64 = "i64"     #X-Registers
    f8 = "f8"       #B-Registers     
    f16 = "f16"     #H-Registers
    f32 = "f32"     #S-Registers
    f64 = "f64"     #D-Registers
    f128 = "f128"   #Q-Registers



class asm_param:
    """
        Assembler Parameter

        :param value:   Value of the parameter
        :param raw:     Raw-Value of the parameter (before init)
        :param ptype:   Parameter-Type (Number, Pointer, Register)
        :param ftype:   Function-Type, indicates if the parameter is an Input-, Output- or General Purpose register.
        :param dtype:   Datatype of the given parameter
    """
    def __init__(self, value):
        """
        Initialize a asm_param by analyzing the given parameter value.

        :param value:   Value of the parameter
        """
        self.raw = value
        self.value = value
        self.ptype = "Sys_unkown" #ParameterType (Number, Pointer (address), Register)
        self.ftype = "Sys_unkown" #FunctionType (Input, Output or GP-Register)
        self.dtype = "Sys_unkown" #DataType (Integer, Float etc.)

        #Preserver Registers (only those 3 are supported for now)
        if value == "lr" or value == "pc" or value == "sp":
            self.ptype = ptype_type.pointer
        
        #Absolute Values
        elif value[0] == "#":
            self.ptype = ptype_type.number
            self.value = value[1:]

        #Registers
        elif value[0] in supported_register_types:
            self.ptype = ptype_type.register
            if value[0] == "w":           #32Bit Integer
                self.dtype = dtype_type.i32
            elif value[0] == "x":         #64Bit Integer
                self.dtype = dtype_type.i64
            elif value[0] == "b":         #Float (128B to 8Bit) incomming
                self.dtype = dtype_type.f8
            elif value[0] == "h":         #Float (128B to 8Bit) incomming
                self.dtype = dtype_type.f16
            elif value[0] == "s":         #Float (128B to 8Bit) incomming
                self.dtype = dtype_type.f32
            elif value[0] == "d":         #Float (128B to 8Bit) incomming
                self.dtype = dtype_type.f64
            elif value[0] == "q":         #Float (128B to 8Bit) incomming
                self.dtype = dtype_type.f128
            
            #new value (absolute value)
            if value[1:] == "zr":       #Zero Register
                    self.value = 0
                    self.ptype = ptype_type.number
            else:
                self.value = int(value[1:])

                #Analyze Input/Output/GP
                if self.value <= 7:
                    self.ftype = ftype_type.input
                elif self.value == 8:
                    self.ftype = ftype_type.output
                else:
                    self.ftype = ftype_type.general_purpose

        #(RAM) Address
        elif value[0] == "[" and value[-1] == "]":
            self.ptype = ptype_type.address
            self.value = value[1:-1]
        
        #Unknown Types
        else:
            self.ptype = ptype_type.unkown




class asm_function:
    def __init__(self, name = ""):
        """
        Inititalize the asm_function

        :param name: name of the function, defaults to ""
        :type name: str, optional
        """
        self.name: str = name
        self.instructions: list[asm_inst] = []
        self.input_parameter: list[asm_param] = []
        self.return_parameter: asm_param = asm_param("INIT")

    def set_name(self, name: str):
        """
        Sets function name of the given function

        :param name: name of the function
        :type name: str
        """
        self.name = name
        
    def add_instruction(self, instruction: asm_inst):
        """
        Adds an instruction to the given asm_function

        :param instruction: asm_ins to add
        :type instruction: asm_inst
        """
        self.instructions.append(instruction)
        for p in instruction.params:
            if p.ptype == ptype_type.register:
                if p.ftype == ftype_type.input:
                    self.input_parameter.append(p)
                elif p.ftype == ftype_type.output:
                    self.return_parameter = p

    def is_empty(self) -> bool:
        """
        gives information about the amount in instructions in the given function
        
        :return: True if no instructions added to the function
        :rtype: bool
        """
        return len(self.instructions) == 0

    def clean(self):
        """
        Cleans the given asm_function by deleting all doubled input parameter.
        A distinction is made between integer and float register ("W0 and X0" isn´t possible while "W0 and H0" is.)
        """
        known_int_register = []
        known_float_register = []
        deletable_params = []
        for i in self.input_parameter:
            if i.dtype == dtype_type.i32 or i.dtype == dtype_type.i64:
                if i.value not in known_int_register:
                    known_int_register.append(i.value)
                else:
                    deletable_params.append(i)
            else:
                if i.value not in known_float_register:
                    known_float_register.append(i.value)
                else:
                    deletable_params.append(i)
        for i in deletable_params:
            self.input_parameter.remove(i)
            
                


def parse_asm(raw_asm):
    instCount = 0
    execformat = ""
    achritecture = ""
    parserStatus = True

    asm_list = []

    asm_raw = raw_asm.splitlines()
    curFunction = "nA"

    asm_fnc = asm_function()
    for i, line in enumerate(asm_raw):
        if "file format" in line:
            format = line.split("file format ")[1].split(" ")
            architecture = format[1]
            execformat = format[0]

        if len(line) >= 17:
            #Instruction
            if line[9] == ":":           #Instruction
                asm = asm_inst()
                asm.function = curFunction
                asm.address = line[:9]
                asm.hexValue = line[10:22].replace(" ", "")
                params = line[24:].split("\t",1)[1]
                if "\t" not in params:  #onlyInstruction
                    asm.instruction = params
                else:
                    p = params.split("\t", 1)
                    asm.instruction = p[0]
                
                    params = p[1].split(", ")
                    tmp = []
                    for i, p in enumerate(params):
                        param = None
                        if p[0] != "[": 
                            if p[-1] == "]":
                                param = asm_param(params[i-1] + ", " + params[i])
                                tmp.append(param)
                            else:
                                param = asm_param(p)
                                tmp.append(param)

                    asm.params = tmp.copy()

                asm_fnc.add_instruction(asm)
                instCount += 1
            elif line[-1] == ":" and "of section" not in line:           #Function
                if not asm_fnc.is_empty():
                    asm_fnc.name = curFunction
                    asm_fnc.clean()
                    asm_list.append(asm_fnc)
                    asm_fnc = asm_function()
                curFunction = line[17:-1]
                
    print("PARSER (Overview) ---------------\n Architecture: \t\t{}\n Executeable Format:\t{} \n Instructions: \t\t{}\n Functions: \t\t{}\n Sucessfull:\t\t{}\n---------------------------------".format(architecture, execformat, instCount, len(asm_list), parserStatus))
    return asm_list


'''
def parse_asm_wh(raw_asm):
    functionCount = 0
    execformat = ""
    achritecture = ""
    parserStatus = True
    asm_list = []

    asm_raw = raw_asm.splitlines()
    curFunction = "nA"

    for line in asm_raw:
        if "file format" in line:
            format = line.split("file format ")[1].split(" ")
            architecture = format[1]
            execformat = format[0]

        if len(line) >= 17:
            #Instruction
            asm = asm_inst()
            asm.function = curFunction
            if line[9] == ":":      #Instruction
                asm.address = line[:9]

                params = line.split("\t", 1)[1]
                if "\t" not in params:  #onlyInstruction
                    asm.instruction = params
                else:
                    p = params.split("\t", 1)
                    asm.instruction = p[0]

                    p_arr = []
                    params = p[1].split(", ")
                    for i, p in enumerate(params):
                        if p[0] != "[": 
                            if p[-1] == "]":
                                p_arr.append(params[i-1] + ", " + params[i])
                            else:
                                p_arr.append(p)
                    
                    asm.params = p_arr
                asm_list.append(asm)

            elif line[17] == "<":   #Function
                curFunction = line[17:-1]
                functionCount += 1
    log()
    print("PARSER (Overview) ---------------\n Architecture: \t\t{}\n Executeable Format:\t{} \n Instructions: \t\t{}\n Functions: \t\t{}\n Sucessfull:\t\t{}\n---------------------------------".format(architecture, execformat, len(asm_list), functionCount, parserStatus))
    return asm_list

'''