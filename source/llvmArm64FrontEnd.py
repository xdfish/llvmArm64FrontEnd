import parser
import disasmler

#SETTINGS
export = False

def generate_llvm_ir_of_arm64(source, target):
    asm_raw = disasmler.decompile(source, export)
    if asm_raw == False:
        return False
    asm_list = parser.parse_asm(asm_raw)

    #TEST ONLY!
    return asm_list