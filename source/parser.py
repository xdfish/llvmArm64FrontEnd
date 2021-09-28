from log import log
from enum import Enum
import os.path
from disasmler import disasembled_raw

""""
TODO:\n
-> Sections unterscheiden, damit man Funktionen mit Namen wie _cstring im Data-Bereich von Funktionen im Text-Bereich abgrenzen kann.\n
-> Konstanten Section in asm_list aufnahmen (aktuell keine implementierung zur Erkennung)\n
-> Input Parameter der Main-Funktion richtig parsen. Aktuell werden R0 bis R7 scheinbar ohne Grund vewendet!?\n
"""

class asm_ptype(Enum):
    """
    Parameter Types
    Describes the type of the parameter (Options below)
    """
    sys_init = "SYS_INIT"
    sp_pointer = "SP_POINTER"
    lr_pointer = "LR_POINTER"
    pc_pointer = "PC_POINTER"
    number = "NUMBER"
    hex_number = "HEX_NUMBER"
    register = "REGISTER"
    address = "ADDRESS"
    sp_address = "SP_ADDRESS"
    fnc_name = "FNC_NAME"
    unkown = "UNKNOWN"

class asm_ftype(Enum):
    """
    Functional Type od the Parameter
    Describes the functional type of the parameter (Options below)
    """
    sys_init = "SYS_INIT"
    input = "INPUT"
    output = "OUTPUT"
    general_purpose = "GP"

class asm_fnctype(Enum):
    sys_fnc = "SYS_FNC"
    user_fnc = "USER_FNC"
    undefined =  "UNDEFINED"
    
class asm_dtype(Enum):
    """
    Possible Datatypes of the ARM-Registers.
    This also provides the supported register for tge parsing process
    """
    sys_init = "SYS_INIT"
    """
    Initial value
    """
    i32 = "w"     #W-Registers
    """
    32Bit Integer (W-Register)
    """
    i64 = "x"     #X-Registers
    """
    64Bit Integer (X-Register)
    """
    f8 = "b"       #B-Registers
    """
    8Bit Float (B-Register)
    """         
    f16 = "h"     #H-Registers
    """
    16Bit Float (H-Register)
    """
    f32 = "s"     #S-Registers
    """
    32Bit Float (S-Register)
    """
    f64 = "d"     #D-Registers
    """
    64Bit Float (D-Register)
    """
    f128 = "q"   #Q-Registers
    """
    128Bit Float (Q-Register)
    """

supported_register_types = set(reg.value for reg in asm_dtype)

class asm_itype(Enum):
    sub = "sub"
    mul = "mul"
    adrp = "adrp"
    udf = "udf"
    adr = "adr"
    ldpsw = "ldpsw"
    ldur = "ldur"
    subs = "subs"
    ldp = "ldp"
    br = "br"
    str = "str"
    ldr = "ldr"
    add = "add"
    ret = "ret"
    mov = "mov"
    stur = "stur"
    bl = "bl"
    stp = "stp"
    nop = "nop"
    sdiv = "sdiv"
    udiv = "udiv"
    b = "b"
    unknown = "<unknown>"

class asm_inst:
    def __init__(self, function : str = "", address : str = "", hexValue : str = "", instruction : asm_itype = asm_itype.unknown, params : list = []):
        """Inititalize a new asm_instruction

        :param function:    Name of the function, defaults to ""
        :type function:     str, optional
        :param address:     Address of the instruction, defaults to ""
        :type address:      str, optional
        :param hexValue:    Hex representation of the instruction, defaults to ""
        :type hexValue:     str, optional
        :param instruction: The instruction itself, defaults to ""
        :type instruction:  str, optional
        :param params:      Parameters of the instruction, defaults to []
        :type params:       list[asm_param], optional
        """
        self.function: str = function
        self.address: str = address
        self.hexValue: str = hexValue
        self.instruction: asm_itype = instruction
        self.params: list[asm_param] = params
    
    def set_instruction(self, instruction: str):
        if instruction in asm_itype._value2member_map_:
            self.instruction = asm_itype(instruction)
        else:
            self.instruction = asm_itype.unknown
            print("Instruction {} not supported".format(instruction))


    def __str__(self) -> str:
        tmp = "{}\t".format(self.instruction)
        for i, p in enumerate(self.params):
            if i > 0:
                tmp += ",\t"
            tmp += "{}".format(p.value)
        return tmp

class asm_param:
    """
        Assembler Parameter

        :param value:   Value of the parameter
        :param raw:     Raw-Value of the parameter (before init)
        :param ptype:   Parameter-Type (Number, Pointer, Register)
        :param ftype:   Function-Type, indicates if the parameter is an Input-, Output- or General Purpose register.
        :param dtype:   Datatype of the given parameter
    """
    def __init__(self, value : str):
        """
        Initialize a asm_param by analyzing the given parameter value.

        :param value:   Value of the parameter
        :type value:    str
        """
        self.raw : str = value
        self.value : any = value
        self.ptype : asm_ptype = asm_ptype.sys_init #ParameterType (Number, Pointer (address), Register)
        self.ftype : asm_ftype = asm_ftype.sys_init #FunctionType (Input, Output or GP-Register)
        self.dtype : asm_dtype = asm_dtype.sys_init #DataType (Integer, Float etc.)

        #Preserver Registers (only those 3 are supported for now)
        if value == "sp":
            self.ptype = asm_ptype.sp_pointer
        elif value == "pc":
            self.ptype = asm_ptype.pc_pointer
        elif value == "lr":
            self.ptype = asm_ptype.lr_pointer
        
        #Absolute Value
        elif value[0] == "#":
            self.ptype = asm_ptype.number
            self.value = value[1:]

        elif value[0] == "_":
            self.ptype = asm_ptype.fnc_name
            self.value = value[1:]

        #Absolute Hex Value
        elif value[0:1] == "0x":
            self.ptype = asm_ptype.hex_number
            self.value = value[2:]

        
        #Register
        elif value[0] in supported_register_types:
            self.ptype = asm_ptype.register
            if value[0] == "w":           #32Bit Integer
                self.dtype = asm_dtype.i32
            elif value[0] == "x":         #64Bit Integer
                self.dtype = asm_dtype.i64
            elif value[0] == "b":         #Float (128B to 8Bit)
                self.dtype = asm_dtype.f8
            elif value[0] == "h":         #Float (128B to 8Bit)
                self.dtype = asm_dtype.f16
            elif value[0] == "s":         #Float (128B to 8Bit)
                self.dtype = asm_dtype.f32
            elif value[0] == "d":         #Float (128B to 8Bit)
                self.dtype = asm_dtype.f64
            elif value[0] == "q":         #Float (128B to 8Bit)
                self.dtype = asm_dtype.f128
            
            #new value (absolute value)
            if value[1:] == "zr":       #Zero Register
                    self.value = 0
                    self.ptype = asm_ptype.number
            else:
                self.value = int(value[1:])

                #Analyze Input/Output/GP
                if self.value <= 7:
                    self.ftype = asm_ftype.input
                elif self.value == 8:
                    self.ftype = asm_ftype.output
                else:
                    self.ftype = asm_ftype.general_purpose

        #(RAM) Address
        elif value[0] == "[" and value[-1] == "]":
            if value[1:3] == "sp":
                self.ptype = asm_ptype.sp_address
            else:
                self.ptype = asm_ptype.address
            self.value = value[1:-1]
        
        #Unknown Type
        else:
            self.ptype = asm_ptype.unkown

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
        self.set_name(name)
        
    def set_name(self, name: str):
        """
        Sets function name of the given function

        :param name: name of the function
        :type name: str
        """
        self.name = name
        self.fnc_type: asm_fnctype = asm_fnctype.undefined
        if len(self.name) > 0:
            if self.name[:2] == "__":
                self.fnc_type: asm_fnctype = asm_fnctype.sys_fnc
            else:
                self.fnc_type: asm_fnctype = asm_fnctype.user_fnc
        
    def add_instruction(self, instruction: asm_inst):
        """
        Adds an instruction to the given asm_function

        :param instruction: asm_ins to add
        :type instruction: asm_inst
        """
        self.instructions.append(instruction)
        for p in instruction.params:
            if p.ptype == asm_ptype.register:
                if p.ftype == asm_ftype.input:
                    self.input_parameter.append(p)
                elif p.ftype == asm_ftype.output:
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
            if i.dtype == asm_dtype.i32 or i.dtype == asm_dtype.i64:
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
    
    def get_address_and_name(self) -> list:
        return [self.instructions[0].address, self.instructions[0].function]
            
class parsed_asm_list:
    """
    Parsed asm list

    :param functions:   list with all asm_functions
    :type functions:    list[asm_function]
    :param const_str:   function with the string constants
    :type const_str:    asm_function
    """
    def __init__(self, filename: str = None, magic: str = None, cputype: str = None, cpu_subtype: str = None, filetype: str = None, sizeofcmds: str = None):
        """
        :param filename: Filename of the parsed assembler file, defaults to None
        :type filename: str, optional
        :param format: format of teh parsed asssembler code, defaults to None
        :type format: str, optional
        :param architecture: architecture of the parsed assembler code, defaults to None
        :type architecture: str, optional
        :param execformat: execution format of the parsed assembler code, defaults to None
        :type execformat: str, optional
        """
        self.filename: str = filename
        self.magic: str = magic
        self.cputype: str = cputype
        self.cpu_subtype: str = cpu_subtype
        self.filetype: str = filetype
        self.sizeofcmds: str = sizeofcmds

        self.function_table: dict = {}
        self.cstring_table: dict = {}
        self.const_table: dict = {}
        self.functions = []

    def set_const_string_with_address(self, address: str, txt: str):
        self.cstring_table[address] = txt

    def set_function_name_with_address(self, address: str, txt: str):
        self.function_table[address] = txt

    def get_const_string_by_address(self, address: str) -> str:
        if address in self.cstring_table:
            return self.cstring_table[address]
        elif address in self.const_table:
            return self.const_table[address]
        else:
            return None
    
    def get_function_name_name_by_address(self, address: str) -> str:
        if address in self.function_table:
            return self.function_table[address]
        else: 
            return None
        
    def append_function(self, function : asm_function):
        """Adds an function to the parsed asm list

        :param function: the function to be added
        :type function: asm_function
        """
        self.functions.append(function)
        if function.name == "__cstring":
            self.const_str = function

def parse_asm(raw_asm: str) -> parsed_asm_list:
    """
    Parses the raw asm_list, which is deliverd by the disabembler

    :param raw_asm: raw_asm list (of disasembler)
    :type raw_asm: str
    :return: Object with parsed asm_functions
    :rtype: parsed_asm_list
    """
    instCount = 0
    execformat = ""
    parserStatus = True

    asm_list = parsed_asm_list()

    asm_raw = raw_asm.splitlines()
    curFunction = "nA"

    asm_fnc = asm_function()
    for i, line in enumerate(asm_raw):
        if "file format" in line:
            filename = line.split(":")[0]
            if "/" in filename:
                filename = filename.split("/")[-1]
            format = line.split("file format ")[1].split(" ")
            architecture = format[1]
            execformat = format[0]

        if len(line) >= 17:  
            #Instruction
            if line[9] == ":":           #Instruction
                asm: asm_inst = asm_inst()
                asm.function = curFunction
                asm.address = line[:9]
                asm.hexValue = line[10:22].replace(" ", "")
                params = line[22:].split("\t",1)[1]
                if "\t" not in params:  #onlyInstruction
                    asm.set_instruction(params)
                else:
                    p = params.split("\t", 1)
                    asm.set_instruction(p[0])

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
                        else:
                            if p[-1] == "]":
                                param = asm_param(p[1:-1])
                                tmp.append(param)
                    asm.params = tmp.copy()

                asm_fnc.add_instruction(asm)
                instCount += 1
            elif line[-1] == ":" and "of section" not in line:           #Function
                if not asm_fnc.is_empty():
                    #For the latest OBJDUMP (on M1 Mac): - -
                    if curFunction[0] == "<" and curFunction[-1] == ">":
                        curFunction = curFunction[1:-1]
                    # - - - - - - - - - - - - - - - - - - - -
                    asm_fnc.set_name(curFunction)
                    asm_fnc.clean()
                    asm_list.append_function(asm_fnc)
                    asm_fnc = asm_function()
                curFunction = line[17:-1]
                
    print("PARSER (Overview) ---------------\n\t|-> Architecture: \t{}\n\t|-> Executeable Format:\t{} \n\t|-> Instructions: \t{}\n\t|-> Functions: \t\t{}\n\t'-> Sucessfull:\t\t{}\n---------------------------------".format(architecture, execformat, instCount, len(asm_list.functions), parserStatus))
    return asm_list

def parse_raw_asm(raw_asm: disasembled_raw) -> parsed_asm_list:
    """
    Parses the raw asm_list, which is deliverd by the disabembler

    :param raw_asm: raw_asm list (of disasembler)
    :type raw_asm: str
    :return: Object with parsed asm_functions
    :rtype: parsed_asm_list
    """
    log(os.path.basename(__file__), "Parsing assembler code of {}".format(raw_asm.filename))
    asm_list: parsed_asm_list = None


    ### HEADER ###
    header_list = " ".join(raw_asm.private_header[-1].split()).split(" ")
    asm_list = parsed_asm_list(filename=raw_asm.filename, magic=header_list[0], cputype=header_list[1], cpu_subtype=header_list[2], filetype=header_list[4], sizeofcmds=header_list[6])
    log(os.path.basename(__file__), "-> private_header (DONE)")

    ### TEXT-SECTION ###
    instCount = 0
    curFunction = "nA"
    asm_fnc = asm_function()
    for i, line in enumerate(raw_asm.text_section):
        #Ignore first two lines (only info)
        if i < 2: 
            continue
        #Functionlabel
        if (line[0] == "_" and line[-1] == ":") or line is raw_asm.text_section[-1]:           
                if not asm_fnc.is_empty():
                    asm_fnc.set_name(curFunction)
                    asm_fnc.clean()
                    asm_list.append_function(asm_fnc)
                    asm_fnc = asm_function()
                curFunction = line[1:-1]
        #Instruction
        else:
            line_l = line.split("\t")
            asm: asm_inst = asm_inst()
            asm.function = curFunction
            asm.address = line_l[0]
            asm.hexValue = line_l[1].replace(" ", "")

            asm.set_instruction(line_l[2])

            #Instruction with parameters
            params = []
            if len(line_l) >= 4:
                params = line_l[3].split(", ")
                tmp = []
                for i, p in enumerate(params):
                    param = None
                    #Stack-address
                    if p[0] == "[" and p[-1] != "]":
                        param = asm_param(p + "_" + params[i+1])
                    else:    
                    #Page-address (adrp)
                        if " ; " in p:
                            param = asm_param(p.split(" ; ")[-1]) 
                    #Register, values etc.
                        else:
                            param = asm_param(p)
                    tmp.append(param)   
                asm.params = tmp.copy()                  
            asm_fnc.add_instruction(asm)
            instCount += 1
    log(os.path.basename(__file__), "-> text_section (DONE)")

    ### CSTRING-SECTION ###
    for i, line in enumerate(raw_asm.cstring_section):
        if i < 2:
            continue
        else:
            asm_list.set_const_string_with_address(line[:16], line[18:])
    log(os.path.basename(__file__), "-> cstring_section (DONE)")

    ### SYMBOL-TABLE ###
    marker: bool = False
    for i, line in enumerate(raw_asm.symbol_table):
        #Skip two title lines
        if "(__" in line and ")" in line and "entries" in line or marker:
            marker = not marker
            continue
        else:
            tmp_line = " ".join(line.split()).split(" ")
            tmp_address = tmp_line[0].split("0x")[-1]
            tmp_fnc_name = tmp_line[-1][1:]
            asm_list.set_function_name_with_address(tmp_address, tmp_fnc_name)
    log(os.path.basename(__file__), "-> symbol_table (DONE)")

    # ADDIOTIONAL FUNCTIONS (NOT DYNAMIC LINKED)
    for f in asm_list.functions:
        tmp = f.get_address_and_name()
        asm_list.set_function_name_with_address(tmp[0], tmp[1])
    log(os.path.basename(__file__), "-> user_functions analyzed (DONE)")

    log(os.path.basename(__file__), "COMPLETE\n")
    return asm_list

