from parser import asm_inst
import irgen
import llvmArm64FrontEnd

asm_register = ["w","x","v"]    #only i32, i64 and float implemented!!!


def analyze_function(asm_fnc):

    #analyze Register, Addresses and Fix Values
    print(asm_fnc.return_parameter)
                

def analyze_asm(asm_list):    
    # for asm_func in asm_list:
    #    analyze_parameter(asm_func)
    if asm_list:
        analyze_function(asm_list[0])
    else:
        print("no asm listing available!")


#TEST
analyze_asm(llvmArm64FrontEnd.generate_llvm_ir_of_arm64("../tmp/prog", ""))