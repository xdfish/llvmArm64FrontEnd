from enum import Enum
from source.irtypes import comdat_types
from source.irtypes import preemption_specifier_types
from source.irtypes import visability_types
from source.irtypes import dll_storage_types


class ir_file:
    def __init__(self, filename):
        self.source_filename = "{}.ll".format(filename)
        self.target_datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
        self.target_triple = "arm64-apple-macosx11.0.0"
        self.global_variables = []
        self.functions = []
        self.declartions = []
        self.attributes = []
        self.flags = []

    def add_source_filename(self, name):
        self.source_filename = name

    def add_target_datalayout(self, datalayout):
        self.target_datalayout = datalayout

    def add_target_triple(self, targettriple):
        self.target_triple = targettriple

    def add_global_variable(self):
        x = 0

    def add_function(self, return_dtype, return_size, name, attribute):
        f = ir_function(return_dtype, return_size, name, attribute)
        self.functions.append(f)
        return f

    def add_declaration(self):
        x=0
    
    def add_attributes(self):
        x=0
    
    def add_flags(self):
        x=0

    def generate(self):
        out = ""

        out += "source_filename = \"{}\"".format(self.source_filename)
        out += "target datalayout = \"{}\"".format(self.target_datalayout)
        out += "target triple = \"{}\"".format(self.target_triple)
        out += "\n"

        for g in self.global_variables:
            out += g.generate()

        for f in self.functions:
            out += f.generate()
        return out
    


# Input Parameter
class inp_param:
    def __init__(self, dtype, size, name):
        self.dtype = dtype
        self.size = int(size)
        self.name = name

    def generate(self):
        return "{}{} {}".format(self.dtype, self.size, self.name)

#Instruction - Allocation 
class inst_allocation:
    def __init__(self, var_name, dtype, size):
        self. var_name = var_name
        self.dtype = dtype
        self.size = int(size)
        self.align = int(self.size/8)

    def generate(self):
        return "{} = alloca {}{}, align {}\n".format(self.var_name, self.dtype, self.size, self.align)

#Instruction Store
class inst_store:
    def __init__(self, source_dtype, source_size, source_name, target_dtype, target_size, target_name):
        self.source_dtype = source_dtype
        self.source_size = int(source_size)
        self.source_name = source_name
        self.target_dtype = target_dtype
        self.target_size = int(target_size)
        self.target_name = target_name
        self.align = int(self.target_size/8)
    
    def generate(self):
        return "store {}{} {}, {}{}* {}, align {}\n".format(self.source_dtype, self.source_size, self.source_name, self.target_dtype, self.target_size, self.target_name, self.align)

class inst_load:
    def __init__(self, target_name, load_dtype, load_size, source_name, source_dtype, source_size):
        self.target_name = target_name
        self.load_dtype = load_dtype
        self.load_size = int(load_size)
        self.source_name = source_name
        self.source_dtype = source_dtype
        self.source_size = int(source_size)
        self.align = int(self.source_size/8)

    def generate(self):
        return "{} = load {}{}, {}{}* {}, align {}\n".format(self.target_name, self.load_dtype, self.load_size, self.source_dtype, self.source_size, self.source_name, self.align)

class inst_add:
    def __init__(self, target, dtype, size, op1, op2, nsw):
        self.target = target
        self.dtype = dtype
        self.size = int(size)
        self.op1 = op1
        self.op2 = op2
        self.nsw = ""
        if nsw == True:
            self.nsw = "nsw "
    
    def generate(self):
        return "{} = add {}{}{} {}, {}\n".format(self.target, self.nsw, self.dtype, self.size, self.op1, self.op2)

class inst_sub:
    def __init__(self, target, dtype, size, op1, op2, nsw):
        self.target = target
        self.dtype = dtype
        self.size = int(size)
        self.op1 = op1
        self.op2 = op2
        self.nsw = ""
        if nsw == True:
            self.nsw = "nsw "
    
    def generate(self):
        return "{} = sub {}{}{} {}, {}\n".format(self.target, self.nsw, self.dtype, self.size, self.op1, self.op2)

class inst_mul:
    def __init__(self, target, dtype, size, op1, op2, nsw):
        self.target = target
        self.dtype = dtype
        self.size = int(size)
        self.op1 = op1
        self.op2 = op2
        self.nsw = ""
        if nsw == True:
            self.nsw = "nsw "
        
    
    def generate(self):
        return "{} = mul {}{}{} {}, {}\n".format(self.target, self.nsw, self.dtype, self.size, self.op1, self.op2)

class inst_call:
    def __init__(self, target, dtype, size, f_name):
        self.target = target
        self.dtype = dtype
        self.size = size
        self.f_name = f_name
        self.param = []

    def add_param(self, dtype, size, name):
        self.param.append(inp_param(dtype, size, name))
    
    def generate(self):
        out = "{} = call {}{} @{}(".format(self.target, self.dtype, self.size, self.f_name)
        for i, p in enumerate(self.param):
            if i == 0:
                out += "{}".format(p.generate())
            else:
                out += ", {}".format(p.generate())
        out += ")\n"
        return out

class inst_return:
    def __init__(self, dtype, size, value):
        self.dtype = dtype
        self.size = int(size)
        self.value = value
    
    def generate(self):
        return "ret {}{} {}\n".format(self.dtype, self.size, self.value)

class ir_function:
    def __init__(self, return_dtype, return_size, name, attribute):
        self.return_dtype = return_dtype
        self.return_size = int(return_size)
        self.name = name
        self.attribute = attribute
        self.input_parameter = []
        self.allocations = []
        self.instructions = []

    # FUNCTIONS
    def add_input_parameter(self, dtype, size, name):
        self.input_parameter.append(inp_param(dtype, size, name))

    def add_allocation(self, var_name, dtype, size):
        self.allocations.append(inst_allocation(var_name, dtype, size))

    def add_store(self, source_dtype, source_size, source_name, target_dtype, target_size, target_name):
        self.instructions.append(inst_store(source_dtype, source_size, source_name, target_dtype, target_size, target_name))

    def add_add(self, target, dtype, size, op1, op2, nsw):
        self.instructions.append(inst_add(target, dtype, size, op1, op2, nsw))

    def add_sub(self, target, dtype, size, op1, op2, nsw):
        self.instructions.append(inst_sub(target, dtype, size, op1, op2, nsw))

    def add_mul(self, target, dtype, size, op1, op2, nsw):
        self.instructions.append(inst_mul(target, dtype, size, op1, op2, nsw))

    def add_call(self, target, dtype, size, f_name):
        f = inst_call(target, dtype, size, f_name)
        self.instructions.append(f)
        return f

    def add_return(self, dtype, size, value):
        self.instructions.append(inst_return(dtype, size, value))


    def generate(self):
        out = "define {}{} @{}(".format(self.return_dtype, self.return_size, self.name)
        for i, p in enumerate(self.input_parameter):
            if i == 0:
                out += "{}".format(p.generate())
            else:
                out += ", {}".format(p.generate())
        out += ") {} {{\n".format(self.attribute)

        for a in self.allocations:
            out += "\t{}".format(a.generate())

        for i in self.instructions:
            out += "\t{}".format(i.generate())
        out += "}\n\n"
        return out




'''
irfile = ir_file("test")
#First Function
func = irfile.add_function("i", 32, "add4", "#0")

func.add_input_parameter("i", 32, 0)
func.add_input_parameter("i", 32, 1)
func.add_input_parameter("i", 32, 2)

func.add_allocation("%3", "i", 32)
func.add_store("i", 32, "%3", "i", 32, "%5")

func.add_allocation("%4", "i", 32)
func.add_add("%2","i", 32, "%0", "%16", True)


fcall = func.add_call("%17", "i", 32, "add4")
fcall.add_param("i", 32, "%12")
fcall.add_param("i", 32, "%13")
fcall.add_param("i", 32, "%14")

func.add_return("i", 32, "%3")


#Second Function
f = irfile.add_function("i", 64, "txbah_asd", "#0")
f.add_input_parameter("i", 32, "0")
f.add_allocation("%2", "i", 32)
f.add_return("i", 32, "%3")


print(irfile.generate())
'''