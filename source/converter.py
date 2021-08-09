from parser import asm_inst
from parser import asm_function
from parser import asm_param

import irgen
import llvmArm64FrontEnd

asm_register = ["w","x","v"]    #only i32, i64 and float implemented!!!


def analyze_function(asm_fnc):

    #analyze Register, Addresses and Fix Values
    print("NEW FUNCTION:")
    print("\tNAME \t\t{}".format(asm_fnc.name))
    print("\tRETURN VALUE: \t\t{}".format(asm_fnc.return_parameter.dtype))
    print("\tINSTRUCTIONS: \t{}".format(len(asm_fnc.instructions)))
    print("\tINPUT PARAMETER: {}\n".format(len(asm_fnc.input_parameter)))

                

def analyze_asm(asm_list):    
    # for asm_func in asm_list:
    #    analyze_parameter(asm_func)
    if asm_list:
        for fnc in asm_list:
            analyze_function(fnc)
    else:
        print("no asm listing available!")


#TEST
analyze_asm(llvmArm64FrontEnd.generate_llvm_ir_of_arm64("../tmp/prog", ""))