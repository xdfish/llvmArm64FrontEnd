from source.log import log
import sys
import os
from pathlib import Path
sys.path.insert(1, './source')

import source.parser as parser
import source.disasmler as disasembler
import source.converter as converter


VERSION = 0.1
OUT_FOLDER_NAME = "out"
CFG_START_ARGS_FILE = "config/args.txt"
CFG_HEAD_FILE = "config/head.txt"

#SETTINGS
export: bool = True
inp_filepath: str = None
out_filename: str = None
export_unkown_asminstr: bool = False
information_level_of_detail: int = 0

def generate_llvm_ir_of_arm64():
    """
    Controls the workflow of the toolchain
    """
    global inp_filepath
    global out_filename

    if not inp_filepath:
        inp_filepath = input("@-> Enter filename(and path): ")
    if not out_filename:
            out_filename = seperate_filename(inp_filepath)
            
    input("@-> Press ENTER to start disassembling file: \{}".format(inp_filepath))
    asm_raw = disasembler.disasembled_raw(inp_filepath, export).disasemble()
    if not asm_raw:
        return
    inp_filepath = seperate_filename(inp_filepath)

    input("@-> Press any key to start parssing")
    asm_parsed = parser.parse_raw_asm(asm_raw)
    if not asm_parsed:
        return
    input("@-> Press any key to start conversiond an ir-generation")
    ir_file = converter.analyze_asm(asm_parsed)
    export_file(out_filename, ir_file.generate())

def run():
    """
    Handles the start arguments
    """
    start_args = sys.argv
    if len(start_args) == 2:
        if start_args[1] == "--version":
            print("{}\n Version: {}".format(load_cfg_txt(CFG_HEAD_FILE), VERSION))
            return
        elif start_args[1] == "--help":
            print("{}\n{}".format(load_cfg_txt(CFG_HEAD_FILE), load_cfg_txt(CFG_START_ARGS_FILE)))
            return
        
    
    global out_filename
    global inp_filepath
    for i, arg in enumerate(start_args):
        if i == 1:
            out_filename = seperate_filename(arg)
            inp_filepath = arg
        if arg == "-o":
                if i != len(start_args) -1:
                    out_filename = seperate_filename(start_args[i+1])
                else: 
                    print('Syntax error: -o needs an additional filename parameter.\nFor example\t-o ex_name\tSet the outputfilename to "ex_name"')
                    return
        if arg == "-x":
            global export_unkown_asminstr
            export_unkown_asminstr = True
        if arg == "-d":
            if i != len(start_args) -1:
                try:
                    global information_level_of_detail
                    information_level_of_detail = int(start_args[i+1])
                except ValueError:
                    print("Syntax error: -d needs an additional INTEGER parameter")
                    return
            else:
                print("Syntax error: -d needs an additional parameter between 0 and 3.\nFor example\t-d 0\tDisables the whole information output")
    print(load_cfg_txt(CFG_HEAD_FILE))
    generate_llvm_ir_of_arm64()
    

def export_file(filename: str, data: str):
    """Exports a file, and the file path (if not exits)

    :param filename: ilename (including path)
    :type filename: str
    :param data: the data in string format
    :type data: str
    """
    #TODO Püfen ob file existiert!
    if not os.path.exists(OUT_FOLDER_NAME):
        os.makedirs(OUT_FOLDER_NAME)
    file_path = "{}/{}.ll".format(OUT_FOLDER_NAME, filename)
    f = open(file_path, 'w')
    f.write(data)
    log(os.path.basename(__file__), "llvm ir file saved: {}".format(file_path))
    #TODO Püfen ob Datei geschrieben werden konnte

def seperate_filename(path: str) -> str:
    """Separates the filename, by removing the path und suffix (if exists)

    :param path: filepath
    :type path: str
    :return: filename (without path and suffix)
    :rtype: str
    """
    tmp = path
    if "/" in path:
        tmp = tmp.split("/")[-1]
    if "." in path:
        tmp = tmp.split(".")[0]
    return tmp

def load_cfg_txt(cfg_file: str) -> str:
    """loads a config txt file (if exists)

    :param cfg_file: name of the config file (inluding cfg folder path)
    :type cfg_file: str
    :return: config file content
    :rtype: str
    """
    if os.path.isfile(cfg_file):
        return open(cfg_file, 'r').read()
    else:
        return "ERROR: NO CONFIG FILE"

run()