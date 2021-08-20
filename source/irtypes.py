from enum import Enum
from os import name

#Languange Reference for LLVM-IR:
    # https://llvm.org/docs/LangRef.html

class linkage_types(Enum):
    """
    LLVM Linkage Types: See https://llvm.org/docs/LangRef.html#linkage for mor informations
    """
    # https://llvm.org/docs/LangRef.html#linkage
    private = "private"
    internal = "internal"
    available_externally = "available_externally"
    linkonce = "linkonce"
    weak = "weak"
    common = "common"
    appending = "appending"
    extern_weak = "extern_weak"
    linkonce_odr = "linkonce_odr"
    weak_odr = "weak_odr"
    external = "external"

class preemption_specifier_types(Enum):
    """
    LLVM Preemption-Specifier Types
    See https://llvm.org/docs/LangRef.html#runtime-preemption-model for mor informations
    """
    # https://llvm.org/docs/LangRef.html#runtime-preemption-model
    dso_preemptable = "dso_preemptable"
    dso_local = "dso_local"

class visability_types(Enum):
    """
    LLVM Visability Types
    See https://llvm.org/docs/BitCodeFormat.html#visibility for more informations
    """
    # https://llvm.org/docs/BitCodeFormat.html#visibility
    default = "default"
    hidden = "hidden"
    protected = "protected"

    # A symbol with internal or private linkage must have default visibility.

class dll_storage_types(Enum):
    """
    LLVM DLL-Storage Types
    See https://llvm.org/docs/LangRef.html#dllstorageclass for more informations
    """
    # https://llvm.org/docs/LangRef.html#dllstorageclass
    dllimport = "dllimport"
    dllexport = "dllexport"

class calling_conventions_types(Enum):
    """
    LLVM Calling-Convention Types
    See https://llvm.org/docs/LangRef.html#callingconv for more informations
    """
    # https://llvm.org/docs/LangRef.html#callingconv
    ccc = "ccc"
    fastcc = "fastcc"
    coldcc = "coldcc"
    cc_10 = "cc 10"
    cc_11 = "cc 11"
    webkit_jscc = "webkit_jscc"
    anyregcc = "anyregcc"
    preserve_mostcc = "preserve_mostcc"
    preserve_allcc = "preserve_allcc"
    cxx_fast_tlscc = "cxx_fast_tlscc"
    tailcc = "tailcc"
    swiftcc = "swiftcc"
    swifttailcc = "swifttailcc"
    cfguard_checkcc = "cfguard_checkcc"
    
class parameter_attribute_types(Enum):
    """
    LLVM Parameter-Attribute Types
    See https://llvm.org/docs/LangRef.html#paramattrs for more informations
    """

    # https://llvm.org/docs/LangRef.html#paramattrs
    zeroext = "zeroext"
    signext = "signext"
    inreg = "inreg"
    byval = "byval" #(<ty>)
    byref = "byref" #(<ty>)
    preallocated = "preallocated" #(<ty>)
    inalloca = "inalloca" #(<ty>)
    sret = "sret" #(<ty>)
    elementtype = "elementtype" #(<ty>)
    align = "align" #<n> or (<ty>)
    noalias = "noalias" 
    nocapture = "nocapture"
    nofree = "nofree"
    nest = "nest"
    returned = "returned"
    nonnull = "nonnull"
    dereferenceable = "dereferenceable" #(<n>)
    dereferenceable_or_null = "dereferenceable_or_null"  #(<n>)
    swiftself = "swiftself"
    swiftasync = "swiftasync"
    swifterror = "swifterror"
    immarg = "immarg"
    noundef = "noundef"
    alignstack = "alignstack"  #(<n>)

class function_attribute_types(Enum):
    """
    LLVM Function-Attribute Types
    See https://llvm.org/docs/LangRef.html#fnattrsfor more informations
    """
    # https://llvm.org/docs/LangRef.html#fnattrs
    alignstack = "alignstack" #(<n>)
    allocsize = "allocsize" #(<EltSizeParam>[, <NumEltsParam>])
    alwaysinline = "alwaysinline"
    builtin = "builtin"
    cold = "cold"
    convergent = "convergent"
    frame_pointer_none = "\"none\""
    frame_pointer_non_leaf = "\"non-leaf\""
    frame_pointer_all = "\"all\""
    hot = "hot"
    inaccessiblememonly = "inaccessiblememonly"
    inaccessiblemem_or_argmemonly = "inaccessiblemem_or_argmemonly"
    inlinehint = "inlinehint"
    jumptable = "jumptable"
    minsize = "minsize"
    naked = "naked"
    no_inline_line_tables = "\"no-inline-line-tables\""
    no_jump_tables = "no-jump-tables"
    nobuiltin = "nobuiltin"
    noduplicate = "noduplicate"
    nofree = "nofree"
    noimplicitfloat = "noimplicitfloat"
    noinline = "noinline"
    nomerge = "nomerge"
    nonlazybind = "nonlazybind"
    noprofile = "noprofile"
    noredzone = "noredzone"
    indirect_tls_seg_refs = "indirect-tls-seg-refs"
    noreturn = "noreturn"
    norecurse = "norecurse"
    willreturn = "willreturn"
    nosync = "nosync"
    nounwind = "nounwind"
    nosanitize_coverage ="nosanitize_coverage"
    null_pointer_is_valid = "null_pointer_is_valid"
    optforfuzzing = "optforfuzzing"
    optnone = "optnone"
    optsize = "optsize"
    patchable_function_prologue_short_redirect = "\"prologue-short-redirect\""
    probe_stack = "probe-stack"
    readnone = "readnone"
    readonly = "readonly"
    stack_probe_size = "\"stack-probe-size\""
    no_stack_arg_probe = "\"no-stack-arg-probe\""
    writeonly = "writeonly"
    argmemonly = "argmemonly"
    returns_twice = "returns_twice"
    safestack = "safestack"
    sanitize_address = "sanitize_address"
    sanitize_memory = "sanitize_memory"
    sanitize_thread = "sanitize_thread"
    sanitize_hwaddress = "sanitize_hwaddress"
    sanitize_memtag = "sanitize_memtag"
    speculative_load_hardening = "speculative_load_hardening"
    speculatable = "speculatable"
    ssp = "ssp"
    sspstrong = "sspstrong"
    sspreq = "sspreq"
    strictfp = "strictfp"
    denormal_fp_math = "\"denormal-fp-math\""
    denormal_fp_math_f32 = "\"denormal-fp-math-f32\""
    thunk = "\"thunk\""
    uwtable = "uwtable"
    nocf_check = "nocf_check"
    shadowcallstack = "shadowcallstack"
    mustprogress = "mustprogress"
    warn_stack_size = "\"warn-stack-size\"" # ="<threshold>"
    vscale_range = "vscale_range" #(<min>[, <max>])

class comdat_types(Enum):
    """
    LLVM Comdat Types
    See https://llvm.org/docs/LangRef.html#langref-comdats more informations
    """
    # https://llvm.org/docs/LangRef.html#langref-comdats
    any = "any"
    exactmatch = "exactmatch"
    largest = "largest"
    nodeduplicate = "nodeduplicate"
    samesize = "samesize"


class ir_dtype(Enum):
    """
    LLVM Data Types (Single Value Types)
    See https://llvm.org/docs/LangRef.html#single-value-types for more informations
    """
    i16 = "i16"
    """
    16-bit integer
    """     
    i32 = "i32"
    """
    32-bit integer.
    """
    i64 = "i64"
    """
    64-bit integer.
    """
    half = "half"
    """
    16-bit floating-point value
    """
    bfloat = "bfloat"
    """
    16-bit “brain” floating-point value (7-bit significand).
    """
    float = "float"
    """
    32-bit floating-point value
    """
    double = "double"
    """
    64-bit floating-point value
    """
    fp128 = "fp128"
    """
    128-bit floating-point value (113-bit significand)
    """
    x86_fp80 = "x86_fp80"
    """
    80-bit floating-point value (X87)
    """
    ppc_fp128 = "ppc_fp128"
    """
    128-bit floating-point value (two 64-bits)
    """

class glob_const_type(Enum):
    """LLVM global constant types"""
    global_ = "global"
    const_ = "const"

class unnamed_local_type(Enum):
    """
    LLVM unnamed local types
    """
    unnamed_addr = "unnamed_addr"
    local_unnamed_addr = "local_unnamed_addr"




def opt(optional_variable: Enum) -> str:
    """
    This function helps to print optional values in LLVM-IR Instructions.
    If the Value, which is passed to the function, is "None" it returns an empty string.
    Otherwise it will return the value with a leading whitespace.

    :param optional_variable: The variable withe the optional value
    :type optional_variable: Enum
    :return: Empty string if optional_variable = None, otherwise value of the optional_variable with leading whitsspace
    :rtype: str
    """
    if optional_variable:
        return " {}".format(optional_variable.value)
    return ""


# Global Variable
class ir_global_variable:
    """
    Class for LLVM global Variables
    None optional values have to be set in the init call!
    For more Informations to global variables in LLVM-IR see:  #https://llvm.org/docs/LangRef.html#global-variables
    """
   
    def __init__(self, global_var_name: str, glob_const: glob_const_type, type: ir_dtype):
        self.global_var_name: str = global_var_name
        self.linkage:linkage_types = None
        self.preemption_specifier: preemption_specifier_types = None
        self.visability : visability_types = None
        self.dll_storage_class: dll_storage_types = None
        self.thread_local: str = None
        self.unnamed_local = None
        self.addr_space: int = None
        self.externally_initialized: bool = None
        self.glob_const: glob_const_type = glob_const
        self.type: ir_dtype = type
        self.inititalizer_constant: any = None
        self.section: str = None
        self.comdat: comdat_types = None
        self.align: int = None
    
    def generate(self) -> str:
        """
        Returns the text representation of the global_variable instance

        :return: Text Representation
        :rtype: str
        """
        out = "@{} ={}{}{}{}{}{}".format(self.global_var_name, opt(self.linkage), opt(self.preemption_specifier), opt(self.visability), opt(self.dll_storage_class), opt(self.thread_local), opt(self.unnamed_local))
        if self.addr_space:
            out += " addrspace({})".format(self.addr_space)
        out += "{}{}{}".format(opt(self.externally_initialized), opt(self.glob_const), opt(self.type))
        if self.inititalizer_constant:
            out += " {}".format(self.inititalizer_constant)
        if self.section:
            out += ", section \"{}\"".format(self.section)
        if self.comdat:
            out += ", comdat {}".format(self.comdat.value)
        if self.align:
            out += ", align {}".format(self.align)
        return "{}\n".format(out)


#IR_PARAMETER (Variables and fix values)
class ir_param:
    def str_rep(self) -> str:
        raise NotImplementedError("you have to implement that function!")

    def str_ty(self) -> str:
        raise NotImplementedError("you have to implement that function!")    

class ir_var(ir_param):
    def __init__(self, ty: ir_dtype, name: str = "", param_attribs: list = []) -> None:
        super().__init__()
        self.ty: ir_dtype = ty
        self.name: str = name
        self.param_attribs: list[parameter_attribute_types] = param_attribs

    def generate_fnc_ret(self) -> str:
        out = ""
        for a in self.param_attribs:
            out += "{} ".format(a.value)
        return out + self.ty.value

    def str_rep(self) -> str:
        return "%{}".format(self.name)
    
    def str_ty(self) -> str:
        return self.ty.value

class ir_val(ir_param):
        def __init__(self, ty: ir_dtype, value: any) -> None:
            super().__init__()
            self.ty: ir_dtype = ty
            self.value: any = value
        
        def str_rep(self) -> str:
            return "{}".format(self.value)
        
        def str_ty(self) -> str:
            return self.ty.value
        
        

#Basic Blocks (Protocoll)
class ir_basic_block:
    def generate(self):
        raise NotImplementedError("you have to implement that function!")

class irbb_alloca(ir_basic_block):
    """    
    Allocation instruction - IR_Basic_Block
    """
    # Num Elements is not supported for now!

    def __init__(self, alloc_var: ir_var, align: int = None):
        super().__init__()
        self.alloc_var: ir_var = alloc_var
        self.align = align

    def generate(self):
        out = "{} = alloca {}".format(self.alloc_var.str_rep(), self.alloc_var.str_ty())
        if self.align:
            out += ", align {}".format(self.align)
        return out

class irbb_store(ir_basic_block):
    """    
    Store instruction - IR_Basic_Block
    """
    def __init__(self, source_var: ir_param, target_var: ir_var, align: int = None): 
        super().__init__()
        self.source_var: ir_param = source_var
        self.target_var: ir_var = target_var
        self.align: int = align
    
    def generate(self):
        out = "store {} {}, {}* {}".format(self.source_var.str_ty(), self.source_var.str_rep(), self.target_var.str_ty(), self.target_var.str_rep())
        if self.align:
            out += ", align {}".format(self.align)
        return out

class irbb_load(ir_basic_block):
    """    
    Load instruction - IR_Basic_Block
    """
    def __init__(self, target_var: ir_var, source_var: ir_var, align: int = None):
        super().__init__()
        self.target_var: ir_var = target_var
        self.source_var: ir_var = source_var
        self.align: int = align

    def generate(self):
        out = "{} = load {}, {}* {}".format(self.target_var.str_rep(), self.target_var.str_ty(), self.source_var.str_ty(), self.source_var.str_rep())
        if self.align:
            out += ", align {}".format(self.align)
        return out

class irbb_return(ir_basic_block):
    """
    Return instruction - IR_Basic_Block
    structs are not supported for now!
    """
    def __init__(self, return_var: ir_param = None) -> None:
        super().__init__()
        self.return_var: ir_param = return_var

    def generate(self):
        out = "ret "
        if self.return_var:
            out += "{} {}".format(self.return_var.str_ty(), self.return_var.str_rep())
        else:
            out += "void"
        return out

class irbb_add(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, nsw: bool = False, nuw: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.nsw: bool = nsw
        self.nuw: bool = nuw
        if( not((result_var.str_ty() is op1_var.str_ty()) and (op1_var.str_ty() is op2_var.str_ty()))):
            print("ATTENTION! The given data types doesnt match! (add instruction: var1: {}, var2: {}".format(op1_var.str_rep(), op2_var.str_rep()))
    
    def generate(self):
        out = "{} = add ".format(self.result_var.str_rep())
        if self.nuw:
            out += "nuw "
        if self.nsw:
            out += "nsw "
        out += "{} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_sub(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, nsw: bool = False, nuw: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.nsw: bool = nsw
        self.nuw: bool = nuw
        if( not((result_var.str_ty() is op1_var.str_ty()) and (op1_var.str_ty() is op2_var.str_ty()))):
            print("ATTENTION! The given data types doesnt match! (sub instruction: var1: {}, var2: {}".format(op1_var.str_rep(), op2_var.str_rep()))
    
    def generate(self):
        out = "{} = sub ".format(self.result_var.str_rep())
        if self.nuw:
            out += "nuw "
        if self.nsw:
            out += "nsw "
        out += "{} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_mul(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, nsw: bool = False, nuw: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.nsw: bool = nsw
        self.nuw: bool = nuw
        if( not((result_var.str_ty() is op1_var.str_ty()) and (op1_var.str_ty() is op2_var.str_ty()))):
            print("ATTENTION! The given data types doesnt match! (mul instruction: var1: {}, var2: {}".format(op1_var.str_rep(), op2_var.str_rep()))
    
    def generate(self):
        out = "{} = mul ".format(self.result_var.str_rep())
        if self.nuw:
            out += "nuw "
        if self.nsw:
            out += "nsw "
        out += "{} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out
    


class ir_function:
    def __init__(self, return_type: ir_var, function_name: str):
        self.linkage:linkage_types = None
        self.preemption_specifier: preemption_specifier_types = None
        self.visability : visability_types = None
        self.dll_storage_class: dll_storage_types = None
        self.cconv: calling_conventions_types = None
        self.return_type: ir_var = return_type           #Name of parameter is gonna be ignored!
        self.function_name: str = function_name
        self.argument_list: list[ir_var] = []
        self.unnamed_local: unnamed_local_type = None
        self.addr_space: int = None
        self.function_attribs: list[function_attribute_types] = []
        self.section: str = None
        self.comdat: comdat_types = None
        self.align: int = None
        self.gc: str = None
        self.prefix: ir_val = None
        self.prologue: None = None #NOT SUPPOTED FOR NOW
        self.personality: bool = None
        self.meta_data: str = None
        self.basic_blocks: list[ir_basic_block] = []
    
    def add_basic_block(self, basic_block: ir_basic_block):
        self.basic_blocks.append(basic_block)

    def generate(self):
        out = "define {}{}{}{}{}{} @{} (".format(opt(self.linkage), opt(self.preemption_specifier), opt(self.visability), opt(self.dll_storage_class), opt(self.cconv), self.return_type.generate_fnc_ret(), self.function_name)
        for i, a in enumerate(self.argument_list):
            if i == 0:
                out += "{} {}".format(a.dtype.value, a.name)
            else:
                out += ", {} {}".format(a.dtype.value, a.name)
        out += "){}".format(opt(self.unnamed_local))
        if self.addr_space:
            out += " addrspace({})".format(self.addr_space)
        for f in self.function_attribs:
            out += " {}".format(f.value)
        if self.section:
            out += ", section \"{}\"".format(self.section)
        if self.comdat:
            out += ", comdat {}".format(self.comdat.value)
        if self.align:
            out += ", align {}".format(self.align)
        if self.gc:
            out += " {}".format(self.gc)
        if self.prefix:
            out += " prefix {} {}".format(self.prefix.dtype.value, self.prefix.value)
        if self.personality:
            out += " personality"
        if self.meta_data:
            out += " #{}".format(self.meta_data)
        out += " {\n"
        for bb in self.basic_blocks:
            out += "\t{}\n".format(bb.generate())
        return out + "}\n"




x = ir_function(ir_var(ir_dtype.i32), "testFunction")
x.add_basic_block(irbb_alloca(ir_var(ir_dtype.i64, "t0"), 4))
x.add_basic_block(irbb_alloca(ir_var(ir_dtype.float, "t1"), 4))
x.add_basic_block(irbb_store(ir_var(ir_dtype.i32, "ab"), ir_var(ir_dtype.i64, "cd"), 4))
x.add_basic_block(irbb_load(ir_var(ir_dtype.i32, "cc"), ir_var(ir_dtype.i32, "bb"), 4))
x.add_basic_block(irbb_return())
print(x.generate())