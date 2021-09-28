from enum import Enum
from pathlib import Path
import copy as cp

import inspect

from .parser import asm_inst
from .parser import asm_function
from .parser import asm_param
from .parser import parsed_asm_list
from .parser import asm_ptype
from .parser import asm_ftype
from .parser import asm_dtype
from .parser import asm_fnctype
from .parser import asm_itype

from .irtypes import ir_dtype, ir_fnc_var, ir_param, ir_var, ir_fnc_ret_var, ir_val, irbb_add, irbb_alloca, irbb_global_declare_variable, irbb_load, irbb_return, irbb_store, irbb_sub, irbb_mul
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

translation_align = {
    asm_dtype.i32 : 4,
    asm_dtype.i64 : 8,
    asm_dtype.f8 : 1,
    asm_dtype.f16 : 2,
    asm_dtype.f32 : 4,
    asm_dtype.f64 : 8,
    asm_dtype.f128 : 16
}

def convert_function(fnc: asm_function) -> ir_function:
    #convert returntype
    ret_dtype: ir_fnc_var = ir_fnc_var(translation_dtype[fnc.return_parameter.dtype])
    
    #set function name
    function_name: str = fnc.name

    #generate function
    fn = ir_function(ret_dtype, function_name)

    #comvert argumentlist
    arg_list: list[ir_var] = []
    for i, ip in enumerate(fnc.input_parameter):
        arg_list.append(ir_var(translation_dtype[ip.dtype], ip.value))
    fn.argument_list = arg_list

    allocated = {}

    #TRANSLATION FOR ADD INSTRUCTION
    def add_store(i: asm_inst):
        t_dtype = translation_dtype[i.params[0].dtype]
        t_align = translation_align[i.params[0].dtype]
        t_target_var = ir_var(t_dtype, i.params[1].value)
        t_source_var = None
        if i.params[0].ptype is asm_ptype.number:
            t_source_var = ir_val(t_dtype, i.params[0].value)
        else:
            t_source_var = ir_var(t_dtype, i.params[0].value)
        
        if t_target_var.str_rep() not in allocated:
            fn.add_basic_block(irbb_alloca(t_target_var, t_align))
            allocated[t_target_var.str_rep()] = None
        fn.add_basic_block(irbb_store(t_source_var, t_target_var))

    #TRANSLATION FOR ADD INSTRUCTION
    def add_load(i: asm_inst):
        t_target_var = i.params[0].value
        t_source_var = i.params[1].value
        t_dtype = translation_dtype[i.params[0].dtype]
        t_align = translation_align[i.params[0].dtype]
        fn.add_basic_block(irbb_load(ir_var(t_dtype, t_target_var), ir_var(t_dtype, t_source_var), t_align))

    #TRANSLATION FOR CALC INSTRUCTION
    def add_calc(i: asm_inst):
        t_dtype = translation_dtype[i.params[0].dtype]
        t_target_var = ir_var(t_dtype, i.params[0].value)
        t_var1 = None
        t_var2 = None
        if i.params[1].ptype is asm_ptype.register:
            t_var1 = ir_var(t_dtype, i.params[1].value)
        elif i.params[1].ptype is asm_ptype.number:
            t_var1 = ir_val(t_dtype, i.params[1].value)
        if i.params[2].ptype is asm_ptype.register:
            t_var2 = ir_var(t_dtype, i.params[2].value)
        elif i.params[2].ptype is asm_ptype.number:
            t_var2 = ir_val(t_dtype, i.params[2].value)
        if i.instruction is asm_itype.add:
            fn.add_basic_block(irbb_add(t_target_var, t_var1, t_var2, True, False))
        elif i.instruction is asm_itype.sub:
            fn.add_basic_block(irbb_sub(t_target_var, t_var1, t_var2, True, False))
        elif i.instruction is asm_itype.sdiv or i.instruction is asm_itype.udiv:
            fn.add_basic_block(irbb_sub(t_target_var, t_var1, t_var2, True, False))
        else:
            fn.add_basic_block(irbb_mul(t_target_var, t_var1, t_var2, True, False))

    #TRANSLATION FOR RETURN INSTRUCTION
    def add_return(i: asm_inst):
        t_dtype = translation_dtype[fnc.return_parameter.dtype]
        t_ret_var = ir_fnc_ret_var(t_dtype)
        fn.add_basic_block(irbb_return(t_ret_var))



    for i in fnc.instructions:
        if i.instruction is asm_itype.str or i.instruction is asm_itype.stur:
            add_store(i)

        if i.instruction is asm_itype.ldr or i.instruction is asm_itype.ldur:   
            add_load(i)

        if i.instruction is asm_itype.add or i.instruction is asm_itype.sub or i.instruction is asm_itype.mul:
            add_calc(i)
        
        if i.instruction is asm_itype.ret:
            add_return(i)

        #There is no equivalent for a move condition. But it will be the same functionality as load/sotre
        if i.instruction is asm_itype.mov:
            if i.params[1].ptype is not asm_ptype.number:
                add_load(i)
            else:
                tmp1 = cp.copy(i.params[0])
                i.params[0] = cp.copy(i.params[1])
                i.params[1] = tmp1
                i.params[0].dtype = i.params[1].dtype #Set dtype to param 0 (cause params[0] is a constant => no dtype)
                add_store(i)

        if i.instruction is asm_itype.bl:
            pass

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
        trig = False
        for p in i.params:
            if p.ptype.value == asm_ptype.sp_pointer.value:
                if i not in removeable:
                    removeable.append(i)
                trig = True
                continue
        if trig:
            continue


        if len(i.params) > 0:
            if i.params[0].ptype.value == asm_ptype.sp_pointer.value:
                removeable.append(i)
                continue
        
        #Rename Variables
        for p in i.params:
            if p.ptype.value is asm_ptype.sp_address.value or p.ptype.value is asm_ptype.address.value:
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

#OUTDATED
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

def analyze_asm(asm_list: parsed_asm_list) -> ir_file:
    if not asm_list:
        print("Converter Error - No parsed asm_list available")
        return
    if not asm_list.filename:
        asm_list.filename = "llvm_conv"
    
    file: ir_file = ir_file(asm_list.filename)

    for const_str in asm_list.cstring_table:
        pass ############ <------<------<-----<------<------<-
    
    for fnc in asm_list.functions:
        if fnc.fnc_type.value == "USER_FNC":
            prepare_for_conversion(fnc)
            converted_fnc = convert_function(fnc)
            file.add_glob_fnc(converted_fnc)
    
    print(file.generate())
    return file
        
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