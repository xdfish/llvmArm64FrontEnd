from source.log import log
import sys
import os
sys.path.insert(1, './source')

import source.parser as parser
import source.disasmler as disasembler
import source.converter as converter


VERSION = 0.1
OUT_FOLDER_NAME = "out"

#SETTINGS
export: bool = True
filename: str = "out"


def generate_llvm_ir_of_arm64():
    log("LLVM-IR FRONT-END FOR ARM64 - VERSION 0.1", "")
    source_file = input("@-> Enter filename: ")
    input("@-> Press any key to start disasembling")
    asm_raw = disasembler.disasembled_raw(source_file, export).disasemble()
    if not asm_raw:
        return
    input("@-> Press any key to start parssing")
    asm_parsed = parser.parse_raw_asm(asm_raw)
    if not asm_parsed:
        return
    input("@-> Press any key to start conversiond an ir-generation")
    ir_file = converter.analyze_asm(asm_parsed)
    export_file(filename, ir_file.generate())

def run():
    generate_llvm_ir_of_arm64()

def export_file(filename: str, data: str):
    #TODO Püfen ob file existiert!
    path = "../{}/{}.ll".format(OUT_FOLDER_NAME, filename)
    f = open(filename, 'w')
    f.write(data)
    log(os.path.basename(__file__), "llvm ir file saved: {}".format(path))
    #TODO Püfen ob Datei geschrieben werden konnte

run()