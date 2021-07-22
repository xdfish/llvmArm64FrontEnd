from parser import asm_inst
import irgen
import llvmArm64FrontEnd

asm_list = llvmArm64FrontEnd.generate_llvm_ir_of_arm64("tmp/prog", "")

asm_register = ["w","x","v"]    #only i32, i64 and float implemented!!!

class register_translation:
    def check_or_add_translation(old_value, new_value):
        if old_value in self.old_values:
            return self.new_values[self.old_values.index(old_value)]
        else:
            self.cur_index = 0
            self.old_values.append(old_value)
            self.new_values.append(new_value)
            return False

class ir_var:
    def __init__(dtype = "", size = 0, name = ""):
        self.dtype = dtype
        self.size = size
        self.name = name

def analyze_parameter(asm_list_function):
    
    params = []

    register = []
    stack_addr = []
    abs_values = []

    input_register = []
    return_register = None

    removeable = []

    return_value = None
    #analyze Register, Addresses and Fix Values
    for i, inst in enumerate(asm_list_function):
        if (i == 0 or i == len(asm_list_function)-2) and (inst.instruction == "sub" or inst.instruction == "add"):
            if inst.params[0] == "sp" and inst.params[1] == "sp":
                removeable.append(i)
                
        for p in inst.params:
            if p not in params:
                params.append(p)
                if p[0] in asm_register:            #Register
                    register.append(p)
                elif p[0] == "[" and p[-1] == "]":  #Stack_address
                    stack_addr.append(p)
                else:                               #absolute_value
                    abs_values.append(p)

    #input Variablen bestimmen
    max_reg_value = 0
    for r in register:
        no = int(r[1])
        if no < 8:
            input_register.append(r)
            if no > max_reg_value:
                max_reg_value = no
        if no == 8: 
            return_register = r
    
    #override adresses with "virtual" registers:
    max_reg_value += 1 #IR-Funtion Label (add one, to avoid compiler errors)

    translation_table = []

    for inst in asm_list_function:
        for p in inst.params:
            if p[0] == "[":
                

def analyze_asm_functions(asm_list):    
    # for asm_func in asm_list:
    #    analyze_parameter(asm_func)
    analyze_parameter(asm_list[0])

analyze_asm_functions(asm_list)

i = ["a","b","c"]
print(i.index("d"))