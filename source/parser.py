from log import log
import os.path

supported_register_types = ["w", "x", "v"]

class asm_inst:
  def __init__(self, function="", address="", hexValue = "", instruction="", params = []):
    self.function = function
    self.address = address
    self.hexValue = hexValue
    self.instruction = instruction
    self.params = params

class asm_param:
    def __init__(self, value):
        self.raw = value
        self.value = value
        if value == "lr" or "pc" or "sp":
            self.type == "POINTER"
        elif value[0] == "#":
            self.type = "NUMBER"
            self.value = value[1:]
        elif value[0] in supported_register_types:
            self.type = "REGISTER"
            if value[0] == "w":
                self.dtype = "i32"
            if value[0] == "x":
                self.dtype = "i64"
            if value[0] == "v":
                self.dtype = "float"
            self.value = int(value[1:])
            
            if value <= 7:
                self.ftype = "INPUT"
            elif value == 8:
                self.ftype = "OUTPUT"
            else:
                self.ftype = "UNKNOWN"

        elif value[0] == "[" and value[-1] == "]":
            self.type = "ADDRESS"
            self.value = value[1:-1]


class asm_function:
    def __init__(self, name = ""):
        self.name = name
        self.instructions = []
        self.input_parameter = []
        self.return_parameter = None

    def set_name(self, name):
        self.name = name
        
    def add_instruction(self, instruction):
        self.instructions.append(instruction)
        for p in instruction.params:
            if p.type == "REGISTER":
                if p.ftype == "INPUT":
                    self.input_parameter.append(p)
                elif p.ftype == "OUTPUT":
                    self.return_parameter = p
                


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

        if len(line) >= 24:
            #Instruction
            if line[9] == ":":           #Instruction
                asm = asm_inst()
                asm.function = curFunction
                asm.address = line[:9]
                asm.hexValue = line[10:22].replace(" ", "")
                params = line[24:]
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
                
                asm_fnc.add_instruction(asm)
                instCount += 1
            elif line[-1] == ":" and "of section" not in line:           #Function
                if len(asm_tmp) != 0:
                    asm_list.append(asm_fnc)
                    asm_tmp = []
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