from source.log import log
import sys
sys.path.insert(1, './source')

import source.parser as parser
import source.disasmler as disasembler
import source.converter as converter

#SETTINGS
export = True

def generate_llvm_ir_of_arm64():
    log("LLVM-IR FRONT-END FOR ARM64 - VERSION 0.1", "")
    source_file = input("@-> Enter filename: ")
    input("@-> Press any key to start disasembling")
    asm_raw = disasembler.disasembled_raw(source_file, export).disasemble()
    source_file = input("@-> Press any key to start parssing")
    if asm_raw == False:
        return False
    asm_parsed = parser.parse_raw_asm(asm_raw)
    source_file = input("@-> Press any key to start conversiond an ir-generation")
    converter.analyze_asm(asm_parsed).generate()

def run():
    generate_llvm_ir_of_arm64()

run()