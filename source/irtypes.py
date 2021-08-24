from enum import Enum
from os import name
import inspect

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
    i1 = "i1"
    i1_ptr = "i1*"
    """
    1-bit integer (mostly used for bool values)
    """     
    i16 = "i16"
    i16_ptr = "i16*"
    """
    16-bit integer
    """     
    i32 = "i32"
    i32_ptr = "i32*"
    """
    32-bit integer.
    """
    i64 = "i64"
    i64_ptr = "i64*"
    """
    64-bit integer.
    """
    half = "half"
    half_ptr = "half*"
    """
    16-bit floating-point value
    """
    bfloat = "bfloat"
    bfloat_ptr = "bfloat*"
    """
    16-bit “brain” floating-point value (7-bit significand).
    """
    float = "float"
    float_ptr = "float*"
    """
    32-bit floating-point value
    """
    double = "double"
    double_ptr = "double*"
    """
    64-bit floating-point value
    """
    fp128 = "fp128"
    fp128_ptr = "fp128*"
    """
    128-bit floating-point value (113-bit significand)
    """
    x86_fp80 = "x86_fp80"
    x86_fp80_ptr = "x86_fp80*"
    """
    80-bit floating-point value (X87)
    """
    ppc_fp128 = "ppc_fp128"
    ppc_fp128_ptr = "ppc_fp128*"
    """
    128-bit floating-point value (two 64-bits)
    """

irgroup_dtype_integer = [ir_dtype.i16, ir_dtype.i32, ir_dtype.i64]
irgroup_dtype_float = [ir_dtype.half, ir_dtype.bfloat, ir_dtype.float, ir_dtype.double, ir_dtype.fp128, ir_dtype.x86_fp80, ir_dtype.ppc_fp128]
    
def dtype_check(params: list, allowed_types: list = None, function: str = "") -> bool:
    """
    Checks if all params are of the same dtype, and if they are allowed

    :param params: List with parameter to check
    :type params: list[ir_param]
    :param allowed_types: List with allowed dtypes, defaults to []
    :type allowed_types: list[ir_dtype], optional
    :param function: Name of the function, which calls the check function, defaults to ""
    :type function: str, optional
    :return: True if all conditions match, False if not (see also text output)
    :rtype: bool
    """

    calling_class = inspect.stack()[1][0].f_locals["self"].__class__.__name__

    last: str  = None
    for p in params:
        if allowed_types and p.ty not in allowed_types:
            print("ATTENTION! Datatype of variable not allowed for this instruction!\n\t'-> [{} instruction - {} is {}]\n".format(calling_class, p.str_rep(), p.str_ty()))
            return False
        if last and (p.str_ty() is not last):
            print("ATTENTION! The given variable data types doesnt match!\n\t'-> [{} instruction - {} is not {}]\n".format(function, p.str_rep(), last))
            return False
        else:
            last = p.str_ty()


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

class fast_math_flags_type(Enum):
    nnan = "nnan"
    ninf = "ninf"
    nsz = "nsz"
    arcp = "arcp"
    contract = "contract"
    afn = "afn"
    reassoc = "reassoc"
    fast = "fast"

class atomic_memory_ordering_constraints_type(Enum):
    unordered = "unordered"
    monotonic = "monotonic"
    acquire = "acquire"
    release = "release"
    acq_rel = "acq_rel"
    seq_cst = "seq_cst"

class atomicrmw_op_type(Enum):
    _xchg = "xchg"
    _add = "add"
    _sub = "sub"
    _and = "and"
    _nand = "nand"
    _or = "or"
    _xor = "xor"
    _max = "max"
    _min = "min"
    _umax = "umax"
    _umin = "umin"
    _fadd = "fadd"
    _fsub = "fsub"

class compare_type(Enum):
    _eq = "eq"          #equal
    _ne = "ne"          #not equal
    _ugt = "ugt"        #unsigned greater than
    _uge = "uge"        #unsigned greater or equal
    _ult = "ult"        #unsigned less than
    _ule = "ule"        #unsigned less or equal
    _sgt = "sgt"        #signed greater than
    _sge = "sge"        #signed greater or equal
    _slt = "slt"        #signed less than
    _sle = "sle"        #signed less or equal

class tail_type(Enum):
    _tail = "tail"
    _musttail = "musttail"
    _notail = "notail"

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

class ir_ptr_var(ir_param):
    def __init__(self, ty: ir_dtype, size: int, ptr: str) -> None:
        super().__init__()
        self.ty: ir_dtype = ty
        self.size: int = size
        self.ptr: str = ""
    


#Basic_Blocks (Protocoll)
class ir_basic_block:
    
    def conditions(self) -> bool:
        #comming soon
        #raise NotImplementedError("you have to implement the conditions() function!")
        pass

    def generate(self):
        raise NotImplementedError("you have to implement the generate() function!")

    def not_supported(self, bb):
        print("ERROR - This instruction is not supported for now: {}".format(bb.__class__.__name__))

#IR_FUNCTION
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

#Basic Blocks (Instructions)
# -> Terminator Instructions
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

class irbb_br(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_switch(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_indirectbr(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_invoke(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_callbr(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_resume(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_catchswitch(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_catchret(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_cleanupret(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_unreachable(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)


# -> Unary Operations
class irbb_fneg(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, fast_math_flags: list = []) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.fast_math_flags: list[fast_math_flags_type] = fast_math_flags
        dtype_check([result_var, op1_var], irgroup_dtype_float)

    def generate(self):
        out = "{} = fneg".format(self.result_var.str_rep())
        for f in self.fast_math_flags:
            out += " {}".format(f.value)
        out += " {} {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out


# -> Binary Operations
class irbb_add(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, nsw: bool = False, nuw: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.nsw: bool = nsw
        self.nuw: bool = nuw
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer,)
    
    def generate(self):
        out = "{} = add ".format(self.result_var.str_rep())
        if self.nuw:
            out += "nuw "
        if self.nsw:
            out += "nsw "
        out += "{} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_fadd(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, fast_math_flags: list = []) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.fast_math_flags: list[fast_math_flags_type] = fast_math_flags
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_float)

    def generate(self):
        out = "{} = fadd".format(self.result_var.str_rep())
        for f in self.fast_math_flags:
            out += " {}".format(f.value)
        out += " {} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_sub(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, nsw: bool = False, nuw: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.nsw: bool = nsw
        self.nuw: bool = nuw
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)
    
    def generate(self):
        out = "{} = sub ".format(self.result_var.str_rep())
        if self.nuw:
            out += "nuw "
        if self.nsw:
            out += "nsw "
        out += "{} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_fsub(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, fast_math_flags: list = []) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.fast_math_flags: list[fast_math_flags_type] = fast_math_flags
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_float)

    def generate(self):
        out = "{} = fsub".format(self.result_var.str_rep())
        for f in self.fast_math_flags:
            out += " {}".format(f.value)
        out += " {} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_mul(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, nsw: bool = False, nuw: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.nsw: bool = nsw
        self.nuw: bool = nuw
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)
    
    def generate(self):
        out = "{} = mul ".format(self.result_var.str_rep())
        if self.nuw:
            out += "nuw "
        if self.nsw:
            out += "nsw "
        out += "{} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_fmul(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, fast_math_flags: list = []) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.fast_math_flags: list[fast_math_flags_type] = fast_math_flags
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_float)

    def generate(self):
        out = "{} = fmul".format(self.result_var.str_rep())
        for f in self.fast_math_flags:
            out += " {}".format(f.value)
        out += " {} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_udiv(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, exact: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.exact: bool = exact
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)

    def generate(self):
        out = "{} = udiv ".format(self.result_var.str_rep())
        if self.exact:
            out += "exact "
        out += "{} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_sdiv(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, exact: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.exact: bool = exact
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)

    def generate(self):
        out = "{} = sdiv ".format(self.result_var.str_rep())
        if self.exact:
            out += "exact "
        out += "{} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_fdiv(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, fast_math_flags: list = []) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.fast_math_flags: list[fast_math_flags_type] = fast_math_flags
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_float)

    def generate(self):
        out = "{} = fdiv".format(self.result_var.str_rep())
        for f in self.fast_math_flags:
            out += " {}".format(f.value)
        out += " {} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_urem(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, exact: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.exact: bool = exact
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)

    def generate(self):
        return "{} = urem {} {}, {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())

class irbb_srem(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, exact: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.exact: bool = exact
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)

    def generate(self):
        return "{} = srem {} {}, {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())

class irbb_frem(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, fast_math_flags: list = []) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.fast_math_flags: list[fast_math_flags_type] = fast_math_flags
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_float)

    def generate(self):
        out = "{} = frem".format(self.result_var.str_rep())
        for f in self.fast_math_flags:
            out += " {}".format(f.value)
        out += " {} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out


# -> Bitwise Binary Operations
class irbb_shl(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, nsw: bool = False, nuw: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.nsw: bool = nsw
        self.nuw: bool = nuw
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)
    
    def generate(self):
        out = "{} = shl ".format(self.result_var.str_rep())
        if self.nuw:
            out += "nuw "
        if self.nsw:
            out += "nsw "
        out += "{} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_lshr(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, exact: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.exact: bool = exact
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)

    def generate(self):
        out = "{} = lshr ".format(self.result_var.str_rep())
        if self.exact:
            out += "exact "
        out += "{} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_ashr(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, exact: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.exact: bool = exact
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)

    def generate(self):
        out = "{} = ashr ".format(self.result_var.str_rep())
        if self.exact:
            out += "exact "
        out += "{} {}, {}".format(self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_and(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, exact: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.exact: bool = exact
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)

    def generate(self):
        return "{} = and {} {}, {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())

class irbb_or(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, exact: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.exact: bool = exact
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)

    def generate(self):
        return "{} = or {} {}, {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())

class irbb_xor(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, exact: bool = False) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.exact: bool = exact
        dtype_check([result_var, op1_var, op2_var], irgroup_dtype_integer)

    def generate(self):
        return "{} = xor {} {}, {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())


# -> Vector Operations
class irbb_insertelement(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_shufflevector(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)


# -> Aggregate Operations
class irbb_extractvalue(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_insertvalue(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)


# -> Memory Access and Addressing Operations
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

class irbb_fence(ir_basic_block):
    def __init__(self, ordering: atomic_memory_ordering_constraints_type, syncscope: str = None) -> None:
        super().__init__()
        self.ordering: atomic_memory_ordering_constraints_type = ordering
        self.syncscope: str = syncscope

    def generate(self):
        out = "fence"
        if self.syncscope:
            out += " syncscope(\"{}\")".format(self.syncscope)
        return out + " {}".format(self.ordering)

class irbb_cmpxchg(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_atomicrmw(ir_basic_block):
    def __init__(self, operation: atomicrmw_op_type, pointer: ir_var, value: ir_val, ordering: atomic_memory_ordering_constraints_type, volatile: bool = False, syncscope: str = None, align: int = None) -> None:
        super().__init__()
        self.operation: atomicrmw_op_type = operation
        self.pointer: ir_var = pointer
        self.value: ir_val = value
        self.ordering: atomic_memory_ordering_constraints_type = ordering
        self.volatile: bool = volatile
        self.syncscope: str = syncscope
        self.align: int = align
    
    def generate(self):
        out = "atomicrmw"
        if self.volatile:
            out += " volatile"
        out += " {} {}* {}, {}".format(self.operation.value, self.pointer.str_ty(), self.pointer.str_rep(), self.value.str_ty(), self.value.str_rep())
        if self.syncscope:
            out += " syncscope(\"{}\")".format(self.syncscope)
        out += " {}".format(self.ordering.value)
        return out + ", align {}".format(self.align)

class irbb_getelementptr(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)


# -> Conversion Operations
class irbb_trunc_to(ir_basic_block):
    def __init__(self, result_var: ir_var, value: ir_val, to_dtype: ir_dtype) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.value: ir_val = value
        self.to_dtype: ir_dtype = to_dtype

        calling_class = self.__class__.__name__
        if (value.ty not in irgroup_dtype_integer) or (to_dtype not in irgroup_dtype_integer):
            print("ATTENTION! This instruction can only convert between integer Datatypes!\n\t'-> [{} instruction - From:{} To:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
        if self.result_var.str_ty() is not to_dtype.value:
            print("ATTENTION! Datatype of result and conversion var does not match!\n\t'-> [{} instruction - Result:{} Conversion:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
    
    def generate(self):
        return "{} = trunc {} {} to {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.value.str_rep(), self.to_dtype.value)

class irbb_zext_to(ir_basic_block):
    def __init__(self, result_var: ir_var, value: ir_val, to_dtype: ir_dtype) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.value: ir_val = value
        self.to_dtype: ir_dtype = to_dtype

        calling_class = self.__class__.__name__
        if (value.ty not in irgroup_dtype_integer) or (to_dtype not in irgroup_dtype_integer):
            print("ATTENTION! This instruction can only convert between integer Datatypes!\n\t'-> [{} instruction - From:{} To:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
        if self.result_var.str_ty() is not to_dtype.value:
            print("ATTENTION! Datatype of result and conversion var does not match!\n\t'-> [{} instruction - Result:{} Conversion:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
    
    def generate(self):
        return "{} = zext {} {} to {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.value.str_rep(), self.to_dtype.value)

class irbb_sext_to(ir_basic_block):
    def __init__(self, result_var: ir_var, value: ir_val, to_dtype: ir_dtype) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.value: ir_val = value
        self.to_dtype: ir_dtype = to_dtype

        calling_class = self.__class__.__name__
        if (value.ty not in irgroup_dtype_integer) or (to_dtype not in irgroup_dtype_integer):
            print("ATTENTION! This instruction can only convert between integer Datatypes!\n\t'-> [{} instruction - From:{} To:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
        if self.result_var.str_ty() is not to_dtype.value:
            print("ATTENTION! Datatype of result and conversion var does not match!\n\t'-> [{} instruction - Result:{} Conversion:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
    
    def generate(self):
        return "{} = sext {} {} to {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.value.str_rep(), self.to_dtype.value)

class irbb_fptrunc_to(ir_basic_block):
    def __init__(self, result_var: ir_var, value: ir_val, to_dtype: ir_dtype) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.value: ir_val = value
        self.to_dtype: ir_dtype = to_dtype

        calling_class = self.__class__.__name__
        if (value.ty not in irgroup_dtype_float) or (to_dtype not in irgroup_dtype_float):
            print("ATTENTION! This instruction can only convert between integer Datatypes!\n\t'-> [{} instruction - From:{} To:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
        if self.result_var.str_ty() is not to_dtype.value:
            print("ATTENTION! Datatype of result and conversion var does not match!\n\t'-> [{} instruction - Result:{} Conversion:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
    
    def generate(self):
        return "{} = fptrunc {} {} to {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.value.str_rep(), self.to_dtype.value)

class irbb_fpext_to(ir_basic_block):
    def __init__(self, result_var: ir_var, value: ir_val, to_dtype: ir_dtype) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.value: ir_val = value
        self.to_dtype: ir_dtype = to_dtype

        calling_class = self.__class__.__name__
        if (value.ty not in irgroup_dtype_float) or (to_dtype not in irgroup_dtype_float):
            print("ATTENTION! This instruction can only convert between integer Datatypes!\n\t'-> [{} instruction - From:{} To:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
        if self.result_var.str_ty() is not to_dtype.value:
            print("ATTENTION! Datatype of result and conversion var does not match!\n\t'-> [{} instruction - Result:{} Conversion:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
    
    def generate(self):
        return "{} = fpext {} {} to {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.value.str_rep(), self.to_dtype.value)

class irbb_fptoui_to(ir_basic_block):
    def __init__(self, result_var: ir_var, value: ir_val, to_dtype: ir_dtype) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.value: ir_val = value
        self.to_dtype: ir_dtype = to_dtype

        calling_class = self.__class__.__name__
        if (value.ty not in irgroup_dtype_float) or (to_dtype not in irgroup_dtype_integer):
            print("ATTENTION! This instruction can only convert between integer Datatypes!\n\t'-> [{} instruction - From:{} To:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
        if self.result_var.str_ty() is not to_dtype.value:
            print("ATTENTION! Datatype of result and conversion var does not match!\n\t'-> [{} instruction - Result:{} Conversion:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
    
    def generate(self):
        return "{} = fptoui {} {} to {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.value.str_rep(), self.to_dtype.value)

class irbb_fptosi_to(ir_basic_block):
    def __init__(self, result_var: ir_var, value: ir_val, to_dtype: ir_dtype) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.value: ir_val = value
        self.to_dtype: ir_dtype = to_dtype

        calling_class = self.__class__.__name__
        if (value.ty not in irgroup_dtype_float) or (to_dtype not in irgroup_dtype_integer):
            print("ATTENTION! This instruction can only convert between integer Datatypes!\n\t'-> [{} instruction - From:{} To:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
        if self.result_var.str_ty() is not to_dtype.value:
            print("ATTENTION! Datatype of result and conversion var does not match!\n\t'-> [{} instruction - Result:{} Conversion:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
    
    def generate(self):
        return "{} = fptosi {} {} to {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.value.str_rep(), self.to_dtype.value)

class irbb_uitofp_to(ir_basic_block):
    def __init__(self, result_var: ir_var, value: ir_val, to_dtype: ir_dtype) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.value: ir_val = value
        self.to_dtype: ir_dtype = to_dtype

        calling_class = self.__class__.__name__
        if (value.ty not in irgroup_dtype_integer) or (to_dtype not in irgroup_dtype_float):
            print("ATTENTION! This instruction can only convert between integer Datatypes!\n\t'-> [{} instruction - From:{} To:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
        if self.result_var.str_ty() is not to_dtype.value:
            print("ATTENTION! Datatype of result and conversion var does not match!\n\t'-> [{} instruction - Result:{} Conversion:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
    
    def generate(self):
        return "{} = uitofp {} {} to {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.value.str_rep(), self.to_dtype.value)

class irbb_sitofp_to(ir_basic_block):
    def __init__(self, result_var: ir_var, value: ir_val, to_dtype: ir_dtype) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.value: ir_val = value
        self.to_dtype: ir_dtype = to_dtype

        calling_class = self.__class__.__name__
        if (value.ty not in irgroup_dtype_integer) or (to_dtype not in irgroup_dtype_float):
            print("ATTENTION! This instruction can only convert between integer Datatypes!\n\t'-> [{} instruction - From:{} To:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
        if self.result_var.str_ty() is not to_dtype.value:
            print("ATTENTION! Datatype of result and conversion var does not match!\n\t'-> [{} instruction - Result:{} Conversion:{}]\n".format(calling_class, result_var.str_ty(), to_dtype.value))
    
    def generate(self):
        return "{} = sitofp {} {} to {}".format(self.result_var.str_rep(), self.result_var.str_ty(), self.value.str_rep(), self.to_dtype.value)

class irbb_ptrtoint_to(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_inttoptr_to(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_bitcast_to(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_addrspacecast_to(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)


# -> Other Operations
class irbb_icmp(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, condition: compare_type) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.condition: compare_type = condition

    def generate(self):
        out = "{} = icmp {} {} {}, {}".format(self.result_var.str_rep(), self.condition.value, self.op1_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())
        return out

class irbb_fcmp(ir_basic_block):
    def __init__(self, result_var: ir_var, op1_var: ir_param, op2_var: ir_param, condition: compare_type, fast_math_flags: list = []) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.op1_var: ir_param = op1_var
        self.op2_var: ir_param = op2_var
        self.condition: compare_type = condition
        self.fast_math_flags: list[fast_math_flags_type] = fast_math_flags

    def generate(self):
        out = "{} = icmp".format(self.result_var.str_rep())
        for f in self.fast_math_flags:
            out += " {}".format(f.value)
        return out + " {} {} {}, {}".format(self.condition.value, self.op1_var.str_ty(), self.op1_var.str_rep(), self.op2_var.str_rep())

class irbb_phi(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_select(ir_basic_block):
    def __init__(self, result_var: ir_var, val1_var: ir_param, val2_var: ir_param, condition: compare_type, fast_math_flags: list = []) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.val1: ir_param = val1_var
        self.val2: ir_param = val2_var
        self.condition = condition
        self.fast_math_flags: list[fast_math_flags_type] = fast_math_flags

    def generate(self) -> str:
        out = "{} = select".format(self.result_var.str_rep())
        for f in self.fast_math_flags:
            out += " {}".format(f.value)
        out += " selty {}, {} {}, {} {}".format(self.condition.value, self.val1.str_ty(), self.val1.str_rep(), self.val2.str_ty(), self.val2.str_rep())
        return out

class irbb_freeze(ir_basic_block):
    def __init__(self, result_var: ir_var, value: ir_var) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.value: ir_var = value
    
    def generate(self) -> str:
        return "{} = freeze {} {}".format(self.result_var.str_rep(), self.value.str_ty(), self.value.str_rep())

class irbb_call(ir_basic_block):
    def __init__(self, result_var: ir_var, fn_ptr: str, fn_args: list, tail: tail_type = None, fast_math_flags: list = [], cconv: calling_conventions_types = None, ret_attrs: list = [], addrspace: int = None, fn_attrs: list = [], operand_bundle: list = []) -> None:
        super().__init__()
        self.result_var: ir_var = result_var
        self.fn_ptr: str = fn_ptr
        self.fn_args:list[ir_var] = fn_args                                  #TODO!!!
        self.tail: tail_type = tail
        self.fast_math_flags: list[fast_math_flags_type] = fast_math_flags
        self.cconv: calling_conventions_types = cconv
        self.ret_attrs: list[parameter_attribute_types] = ret_attrs
        self.addrspace: int = addrspace
        self.fn_attrs: list[function_attribute_types] = fn_attrs
        self.operand_bundle = operand_bundle                    #NOT SUPPORTED FOR NOW!
        if len(self.operand_bundle) is not 0:
            print("ATTENTION -> Operation Bundles in function calls are not supported for now!")
        
    def generate(self):
        out = "{} =".format(self.result_var.str_rep())
        if self.tail:
            out += " {}".format(self.tail.value)
        out += " call"
        for f in self.fast_math_flags:
            out += " {}".format(f.value)
        if self.cconv:
            out += " {}".format(self.cconv.value)
        for r in self.ret_attrs:
            out += " {}".format(r.value)
        if self.addrspace:
            out += " addrspace({})".format(self.addrspace)
        out += " {} @{}(".format(self.result_var.str_ty(), self.fn_ptr)
        for i, fa in enumerate(self.fn_args):
            tmp = "{} {}".format(fa.str_ty(), fa.str_rep())
            if i is not 0:
                tmp = ", " + tmp
            out += tmp
        out += ")"
        for fa in self.fn_attrs:
            out += " {}".format(fa.value)
        return out
        #operand bundle NOT supported

class irbb_va_arg(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_landingpad(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported()

class irbb_catchpad(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_cleanuppad(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)


# -> Intrinsic Functions
# Variable Argument Handling Intrinsics
class irbb_llvm_va_start(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_llvm_va_end(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)

class irbb_llvm_va_copy(ir_basic_block):
    def __init__(self) -> None:
        super().__init__()
        super().not_supported(self)



x = ir_function(ir_var(ir_dtype.i32), "testFunction")
x.add_basic_block(irbb_alloca(ir_var(ir_dtype.i64, "t0"), 4))
x.add_basic_block(irbb_alloca(ir_var(ir_dtype.float, "t1"), 4))
x.add_basic_block(irbb_store(ir_var(ir_dtype.i32, "ab"), ir_var(ir_dtype.i64, "cd"), 4))
x.add_basic_block(irbb_load(ir_var(ir_dtype.i32, "cc"), ir_var(ir_dtype.i32, "bb"), 4))
x.add_basic_block(irbb_add(ir_var(ir_dtype.i32, "o"), ir_var(ir_dtype.i32, "l"), ir_var(ir_dtype.i32, "p"), True))
x.add_basic_block(irbb_fadd(ir_var(ir_dtype.float, "j"), ir_var(ir_dtype.float, "n"), ir_val(ir_dtype.float, "4.0"), [fast_math_flags_type.nnan, fast_math_flags_type.afn]))
x.add_basic_block(irbb_atomicrmw(atomicrmw_op_type._add, ir_var(ir_dtype.i32, "k"), ir_val(ir_dtype.i32, "5"), atomic_memory_ordering_constraints_type.acquire, True, "test", 3))
x.add_basic_block(irbb_return())
x.add_basic_block(irbb_call(ir_var(ir_dtype.i32, "2"), "add4", [ir_var(ir_dtype.i16, "a"), ir_var(ir_dtype.float, "b")], tail_type._musttail, [], calling_conventions_types.cc_10, [], 4, [], []))
print(x.generate())

y = irbb_insertelement()