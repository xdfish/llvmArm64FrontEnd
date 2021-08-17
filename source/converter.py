from enum import Enum

from source.parser import asm_inst
from source.parser import asm_function
from source.parser import asm_param
from source.parser import parsed_asm_list
from source.parser import asm_type_ptype
from source.parser import asm_type_ftype
from source.parser import asm_type_dtype

detail_count = 1
detail_show = True


def prepare_for_conversion(fnc: asm_function):
    translation = {}
    removeable: list[asm_inst] = []

    for i in fnc.instructions:
        #Mark removeable Stackpointer operations
        if len(i.params) > 0:
            if i.params[0].ptype.value == asm_type_ptype.sp_pointer.value:
                removeable.append(i)
                continue
        
        #Rename Variables
        for p in i.params:
            if p.ptype.value is asm_type_ptype.sp_address.value:
                if p.value not in translation:
                    translation[p.value] = "t{}".format(len(translation))
                p.value = translation[p.value]
            elif p.ptype.value is asm_type_ptype.register.value:
                p.value = "r{}".format(p.value) 
    #Remove marked instructions
    for r in removeable:
        fnc.instructions.remove(r)            

    if detail_show:
        show_details_prepare(fnc.name, len(removeable), translation)



def analyze_function(fnc: asm_function):
    if detail_show:
        show_details_overview(fnc)
    prepare_for_conversion(fnc)



def clean_function(fnc: asm_function):
    """
    Removes all (for the llvm-ir representation) unnecessary instructions and commands of the function

    :param fnc: [description]
    :type fnc: asm_function
    """
    return
    

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
    
    global_str_const = analyze_str_constants(asm_list)

    for fnc in asm_list.functions:
        analyze_function(fnc)


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