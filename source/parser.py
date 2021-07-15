from log import log
import os.path

class asm_inst:
  def __init__(self, function="", address="", hexValue = "", instruction="", params = []):
    self.function = function
    self.address = address
    self.hexValue = hexValue
    self.instruction = instruction
    self.params = params


def parse_asm(raw_asm):
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

        if len(line) >= 24:
            #Instruction
            if line[9] == ":":           #Instruction
                asm = asm_inst()
                asm.function = curFunction
                asm.address = line[:9]
                asm.hexValue = line[10:22].replace(" ", "")
                params = line[23:-1]
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
            elif line[17] == "<":       #Function
                curFunction = line[17:-1]
                functionCount += 1
    print("PARSER (Overview) ---------------\n Architecture: \t\t{}\n Executeable Format:\t{} \n Instructions: \t\t{}\n Functions: \t\t{}\n Sucessfull:\t\t{}\n---------------------------------".format(architecture, execformat, len(asm_list), functionCount, parserStatus))
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