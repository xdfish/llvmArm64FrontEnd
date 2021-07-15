class asm_inst:
  def __init__(self, function="", address="", instruction="", params = []):
    self.function = function
    self.address = address
    self.instruction = instruction
    self.params = params

def parseASM():
    with open('tmp/tmp.asm', 'r') as f:
        data = f.read()
        asm_raw = data.splitlines()

    functionCount = 0
    execformat = ""
    achritecture = ""
    parserStatus = True

    asm_list = []

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

    print("PARSER (Overview) ---------------\n Architecture: \t\t{}\n Executeable Format:\t{} \n Instructions: \t\t{}\n Functions: \t\t{}\n Sucessfull:\t\t{}\n---------------------------------".format(architecture, execformat, len(asm_list), functionCount, parserStatus))
    return asm_list