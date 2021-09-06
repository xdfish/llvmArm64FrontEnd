from enum import Enum
from pathlib import Path
print(Path(__file__).stem)

import inspect

from .parser import asm_inst
from .parser import asm_function
from .parser import asm_param
from .parser import parsed_asm_list
from .parser import asm_ptype
from .parser import asm_ftype
from .parser import asm_dtype
from .parser import asm_fnctype

from .irtypes import ir_dtype, ir_fnc_var, ir_var
from .irtypes import ir_file
from .irtypes import ir_function

detail_count = 1
detail_show = True

translation_dtype = {
    asm_dtype.i32 : ir_dtype.i32,
    asm_dtype.i64 : ir_dtype.i64,
    asm_dtype.f8 : ir_dtype.half,
    asm_dtype.f16 : ir_dtype.half,
    asm_dtype.f32 : ir_dtype.float,
    asm_dtype.f64 : ir_dtype.double,
    asm_dtype.f128 : ir_dtype.fp128,
    asm_dtype.sys_init : ir_dtype.NONE
}

def convert_function(fnc: asm_function) -> ir_function:
    ret_dtype: ir_fnc_var = ir_fnc_var(translation_dtype[fnc.return_parameter.dtype])
    function_name: str = fnc.name

    fn = ir_function(ret_dtype, function_name)

    arg_list: list[ir_var] = []
    for i, ip in enumerate(fnc.input_parameter):
        arg_list.append(ir_var(translation_dtype[ip.dtype], ip.value))

    fn.argument_list = arg_list
    return fn
    
def prepare_for_conversion(fnc: asm_function):
    """
    Perparation for the conversion performs a clean process (deleting unnecessary parts of the asm code) and a renaming of all variables
    :param fnc: assembler function (see: parser.asm_function)
    :type fnc: asm_function
    """
    if detail_show:
        show_details_overview(fnc)

    variable_translation_table = {}
    removeable: list[asm_inst] = []

    for i in fnc.instructions:
        #Mark removeable Stackpointer operations
        if len(i.params) > 0:
            if i.params[0].ptype.value == asm_ptype.sp_pointer.value:
                removeable.append(i)
                continue
        
        #Rename Variables
        for p in i.params:
            if p.ptype.value is asm_ptype.sp_address.value:
                if p.value not in variable_translation_table:
                    variable_translation_table[p.value] = "t{}".format(len(variable_translation_table))
                p.value = variable_translation_table[p.value]
            elif p.ptype.value is asm_ptype.register.value:
                p.value = "r{}".format(p.value)

    #Remove marked instructions
    for r in removeable:
        fnc.instructions.remove(r)            

    if detail_show:
        show_details_prepare(fnc.name, len(removeable), variable_translation_table)
    
    return fnc

def analyze_str_constants(asm_list: parsed_asm_list) -> list:
    """
    Analyzes the __cstring section of the parsed asm list and returns the string constant in it

    :param asm_list: parsed asm list, with the strong section in it
    :type asm_list: parsed_asm_list
    :return: a list of bytearrays with the single strings
    :rtype: list[bytearray]
    """
    if asm_list.const_str:
       #Not the best implementation. Better split the string in every loop
        tmp_str = bytearray()
        for i in asm_list.const_str.instructions:
            tmp_str.extend(bytearray.fromhex(i.hexValue))
        tmp: list[bytearray] = tmp_str.split(bytearray(b'\x00'))[:-1]
        #decode bytearray to str with: ba_var.decode()
        return tmp

def analyze_asm(asm_list: parsed_asm_list):
    if not asm_list:
        print("Converter Error - No parsed asm_list available")
        return
    if not asm_list.filename:
        asm_list.filename = "llvm_conv"
    
    file: ir_file = ir_file(asm_list.filename)

    global_str_const: list[bytearray] = analyze_str_constants(asm_list)
    
    for fnc in asm_list.functions:
        if fnc.fnc_type.value == "USER_FNC":
            prepare_for_conversion(fnc)
            converted_fnc = convert_function(fnc)
            file.add_glob_fnc(converted_fnc)
    
    print(file.generate())
        



def show_details_prepare(function_name, removeable_count, translation):
    print("  Preparation Overview for {}".format(function_name))
    print("\t|-> Del. Instructions:\t{}".format(removeable_count))
    print("\t'-> Renamed variables:\t{}\n".format(len(translation)))
    
    if len(translation) > 0:
        print("\tVariables renametable:")
        for t in translation:
            print("\t{} -> {}".format(t, translation[t]))
        print("\n")
    print("---------------------------------")

def show_details_overview(asm_fnc: asm_function):
    """
    Prints function details, of the parsed asm_functions

    :param asm_fnc: The function to be analyzed
    :type asm_fnc: asm_fnc
    """
    global detail_count
    print("CONVERTER (Overview) ------------")
    print("  {}. Function:".format(detail_count))
    print("\t|-> Name \t\t{}".format(asm_fnc.name))
    print("\t|-> Return Type: \t{}".format(asm_fnc.return_parameter.dtype))
    print("\t|-> Instructions: \t{}".format(len(asm_fnc.instructions)))
    print("\t'-> Input Parameter: \t{}\n".format(len(asm_fnc.input_parameter)))
    detail_count += 1