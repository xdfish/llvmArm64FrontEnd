import sys
sys.path.insert(1, './source')

import parser
import disasmler
import converter

#SETTINGS
export = False

def generate_llvm_ir_of_arm64(source, target):
    asm_raw = disasmler.decompile(source, export)
    if asm_raw == False:
        return False
    asm_list = parser.parse_asm(asm_raw)
    
    converter.analyze_asm(asm_list)

#TEST
generate_llvm_ir_of_arm64("./tmp/prog", "./tmp/")