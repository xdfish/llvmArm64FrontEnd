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
    frame_pointer_none = "\"frame-pointer\"=\"none\""
    frame_pointer_non_leaf = "\"frame-pointer\"=\"non-leaf\""
    frame_pointer_all = "\"frame-pointer\"=\"all\""
    hot = "hot"
    inaccessiblememonly = "inaccessiblememonly"
    inaccessiblemem_or_argmemonly = "inaccessiblemem_or_argmemonly"
    inlinehint = "inlinehint"
    jumptable = "jumptable"
    minsize = "minsize"
    naked = "naked"
    no_inline_line_tables_true = "\"no-inline-line-tables\"=\"true\""
    no_inline_line_tables_false = "\"no-inline-line-tables\"=\"false\""
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
    """
    1-bit integer (mostly used for bool values)
    """     
    i1_ptr = "i1*"
    """
    Pointer 1-bit integer (mostly used for bool values)
    """     
    i16 = "i16"
    """
    16-bit integer
    """   
    i16_ptr = "i16*"
    """
    Pointer 16-bit integer
    """     
    i32 = "i32"
    """
    32-bit integer.
    """
    i32_ptr = "i32*"
    """
    Pointer 32-bit integer.
    """
    i64 = "i64"
    """
    64-bit integer.
    """
    i64_ptr = "i64*"
    """
    Pointer 64-bit integer.
    """
    half = "half"
    """
    16-bit floating-point value
    """
    half_ptr = "half*"
    """
    Pointer 16-bit floating-point value
    """
    bfloat = "bfloat"
    """
    16-bit “brain” floating-point value (7-bit significand).
    """
    bfloat_ptr = "bfloat*"
    """
    Pointer 16-bit “brain” floating-point value (7-bit significand).
    """
    float = "float"
    """
    32-bit floating-point value
    """
    float_ptr = "float*"
    """
    Pointer 32-bit floating-point value
    """
    double = "double"
    """
    64-bit floating-point value
    """
    double_ptr = "double*"
    """
    Pointer 64-bit floating-point value
    """
    fp128 = "fp128"
    """
    128-bit floating-point value (113-bit significand)
    """
    fp128_ptr = "fp128*"
    """
    Pointer 128-bit floating-point value (113-bit significand)
    """
    x86_fp80 = "x86_fp80"
    """
    80-bit floating-point value (X87)
    """
    x86_fp80_ptr = "x86_fp80*"
    """
    Pointer 80-bit floating-point value (X87)
    """
    ppc_fp128 = "ppc_fp128"
    """
    128-bit floating-point value (two 64-bits)
    """
    ppc_fp128_ptr = "ppc_fp128*"
    """
    Pointer 128-bit floating-point value (two 64-bits)
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

class thread_local_type(Enum):
    localdynamic = "localdynamic"
    initialexec = "initialexec"
    localexec = "localexec"

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

class target_datalayout_mangling_type(Enum):
    elf = "e"
    """ELF mangling"""
    mips = "m"
    """Mips mangling"""
    macho = "o"
    """Mach-O mangling"""
    win_x86_coff = "x"
    """Windows x86 COFF mangling"""
    win_coff = "w"
    """Windows COFF mangling"""
    xcoff = "a"
    """XCOFF mangling"""

class target_datalayout_addr_space:
    def __init__(self, values: list) -> None:
        self.values: list[str] = values

    def generate(self):
        out = ""
        for i, s in enumerate(self.sizes):
            tmp = "{}"
            if i != 0:
                tmp = ":" + tmp
            out += tmp
        return out

class target_datalayout_ptr_align:
    def __init__(self, size: int, abi: int, pref: int = None, idx: int = None) -> None:
        self.size: int = size
        self.abi: int = abi
        self.pref: int = pref
        self.idx: int = idx

    def generate(self):
        out = "p[n]:{}:{}".format(self.size, self.abi)
        if self.pref:
            out += ":{}".format(self.pref)
        if self.idx:
            out += ":{}".format(self.idx)
        return out

class target_datalayout_int_align:
    def __init__(self, size: int, abi: int, pref: int = None) -> None:
        self.size: int = size
        self.abi: int = abi
        self.pref: int = pref

    def generate(self):
        out = "i{}:{}".format(self.size, self.abi)
        if self.pref:
            out += ":{}".format(self.pref)
        return out

class target_datalayout_vector_align:
    def __init__(self, size: int, abi: int, pref: int = None) -> None:
        self.size: int = size
        self.abi: int = abi
        self.pref: int = pref
    
    def generate(self):
        out = "v{}:{}".format(self.size, self.abi)
        if self.pref:
            out += ":{}".format(self.pref)
        return out

class target_datalayout_float_align:
    def __init__(self, size: int, abi: int, pref: int = None) -> None:
        self.size: int = size
        self.abi: int = abi
        self.pref: int = pref
    
    def generate(self):
        out = "f{}:{}".format(self.size, self.abi)
        if self.pref:
            out += ":{}".format(self.pref)
        return out

class target_datalayout_obj_align:
    def __init__(self, abi: int, pref: int = None) -> None:
        self.abi: int = abi
        self.pref: int = pref
    
    def generate(self):
        out = "a:{}".format(self.abi)
        if self.pref:
            out += ":{}".format(self.pref)
        return out

class target_datalayout_fnc_align:
    def __init__(self, type: str, abi: int) -> None:
        self.type = type
        self.abi: int = abi
    
    def generate(self):
        out = "F{}{}".format(self.type, self.abi)
        return out

class target_datalayout_native_i_width:
    def __init__(self, sizes: list) -> None:
        self.sizes: list[int] = sizes
    
    def generate(self):
        out = "n"
        for i, s in enumerate(self.sizes):
            tmp = "{}"
            if i != 0:
                tmp = ":" + tmp
            out += tmp
        return out

class target_tripple_architecture_type(Enum):
    x86_64 = "x86_64"
    arm64 = "arm64"

class target_tripple_vendor_type(Enum):
    apple = "apple"

class target_tripple_operating_system_type(Enum):
    macosx10_15_7 = "macosx10.15.7"
    macosx11_0_0 = "macosx11.0.0"

class module_flag_type(Enum):
    """
    https://llvm.org/docs/LangRef.html#module-flags-metadata
    """
    error = "1"
    warning = "2"
    require = "3"
    override = "4"
    append = "5"
    append_unique = "6"
    max = "7"


# Help-Function - only for optional Enums
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

class ir_fnc_var(ir_param):
    def __init__(self, ty: ir_dtype, param_attribs: list = []) -> None:
        super().__init__()
        self.ty: ir_dtype = ty
        self.param_attribs: list[parameter_attribute_types] = param_attribs

    def str_rep(self) -> str:
        out = ""
        for a in self.param_attribs:
            out += "{} ".format(a.value)
        return out + self.ty.value

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


# Declarations
class irbb_global_declare_variable:
    """
    Class for LLVM global Variables
    None optional values have to be set in the init call!
    For more Informations to global variables in LLVM-IR see:  #https://llvm.org/docs/LangRef.html#global-variables
    """
    
    def __init__(self, global_var: ir_var, glob_const: glob_const_type, linkage: linkage_types = None, preemption_specifier: preemption_specifier_types = None, visability : visability_types = None, dll_storage_class: dll_storage_types = None, thread_local: thread_local_type = None, unnamed_local: unnamed_local_type = None, addr_space: int = None, externally_initialized: bool = False, inititalizer_constant: any = None, section: str = None, comdat: comdat_types = None, align: int = None):
        self.global_var: ir_var = global_var
        self.linkage:linkage_types = linkage
        self.preemption_specifier: preemption_specifier_types = preemption_specifier
        self.visability : visability_types = visability
        self.dll_storage_class: dll_storage_types = dll_storage_class
        self.thread_local: thread_local_type = thread_local
        self.unnamed_local: unnamed_local_type = unnamed_local
        self.addr_space: int = addr_space
        self.externally_initialized: bool = externally_initialized
        self.glob_const: glob_const_type = glob_const
        self.inititalizer_constant: any = inititalizer_constant
        self.section: str = section
        self.comdat: comdat_types = comdat
        self.align: int = align
    
    def generate(self) -> str:
        """
        Returns the text representation of the global_variable instance

        :return: Text Representation
        :rtype: str
        """
        out = "@{} ={}{}{}{}{}{}".format(self.global_var.str_rep(), opt(self.linkage), opt(self.preemption_specifier), opt(self.visability), opt(self.dll_storage_class), opt(self.thread_local), opt(self.unnamed_local))
        if self.addr_space:
            out += " addrspace({})".format(self.addr_space)
        out += "{}{}{}".format(opt(self.externally_initialized), opt(self.glob_const), opt(self.global_var.str_ty()))
        if self.inititalizer_constant:
            out += " {}".format(self.inititalizer_constant)
        if self.section:
            out += ", section \"{}\"".format(self.section)
        if self.comdat:
            out += ", comdat {}".format(self.comdat.value)
        if self.align:
            out += ", align {}".format(self.align)
        return "{}\n".format(out)

class irbb_global_declare_function:
    def __init__(self, return_var: ir_fnc_var, function_name: str, linkage:linkage_types = None, visability : visability_types = None, dll_storage_class: dll_storage_types = None, cconv: calling_conventions_types = None, argument_list: list = [], unnamed_local: unnamed_local_type = None, addr_space: int = None, align: int = None, gc: str = None, prefix: ir_val = None, prologue: None = None):
        self.linkage:linkage_types = linkage
        self.visability : visability_types = visability
        self.dll_storage_class: dll_storage_types = dll_storage_class
        self.cconv: calling_conventions_types = cconv
        self.return_var: ir_fnc_var = return_var           #Name of parameter is gonna be ignored!
        self.function_name: str = function_name
        self.argument_list: list[ir_fnc_var] = argument_list
        self.unnamed_local: unnamed_local_type = unnamed_local
        self.addr_space: int = addr_space
        self.align: int = align
        self.gc: str = gc
        self.prefix: ir_val = prefix
        self.prologue: None = prologue #NOT SUPPOTED FOR NOW

    def generate(self):
        out = "declare {}{}{}{}{} @{}(".format(opt(self.linkage), opt(self.visability), opt(self.dll_storage_class), opt(self.cconv), self.return_var.str_rep(), self.function_name)
        for i, a in enumerate(self.argument_list):
            tmp = "{} {}".format(a.str_ty(), a.str_rep())
            if i != 0:
                tmp = ", " + tmp
            out += tmp
        out += "){}".format(opt(self.unnamed_local))
        if self.addr_space:
            out += " addrspace({})".format(self.addr_space)
        if self.align:
            out += ", align {}".format(self.align)
        if self.gc:
            out += " {}".format(self.gc)
        if self.prefix:
            out += " prefix {} {}".format(self.prefix.dtype.value, self.prefix.value)
        return out

class ir_global_attribs:
    def add_attribute(self):
        raise NotImplementedError("you have to implement the generate() function!")

    def add_attributes(self):
        raise NotImplementedError("you have to implement the generate() function!")
    
    def rename(self):
        raise NotImplementedError("you have to implement the generate() function!")

    def generate(self):
        raise NotImplementedError("you have to implement the generate() function!")

class ir_global_attribs_function(ir_global_attribs):
    def __init__(self, name: str, attribs: list) -> None:
        self.name: str = name
        self.attribs: list[function_attribute_types] = attribs

    def add_attribute(self, attribute: function_attribute_types):
        self.add_attributes([attribute])
    
    def add_attributes(self, attributes: list):
        self.attribs = list(set(self.attribs + attributes))

    def rename(self, name: str):
        self.name: str = name

    def generate(self):
        out = "attributes #{} = {".format(self.name)
        for a in self.attribs:
            out += " {}".format(a.value)
        return out + " }"

class ir_global_attribs_parameter(ir_global_attribs):
    def __init__(self, name: str, attribs: list) -> None:
        self.name: str = name
        self.attribs: list[parameter_attribute_types] = attribs

    def add_attribute(self, attribute: parameter_attribute_types):
        self.add_attributes([attribute])
    
    def add_attributes(self, attributes: list):
        self.attribs = list(set(self.attribs + attributes))
    
    def rename(self, name: str):
        self.name: str = name

    def generate(self):
        out = "attributes #{} = {".format(self.name)
        for a in self.attribs:
            out += " {}".format(a.value)
        return out + " }"

class ir_global_metadata_module_flags:
    #!<name> = !{ i32 <type>, !"<id>", <value_ty, value_val> }
    def __init__(self, name: str, type: module_flag_type, id: str, value: ir_val) -> None:
        self.name: str = name
        self.type: module_flag_type = type
        self.id: str = id
        self.value: ir_val = value

    def str_rep(self):
        return "!{}".format(self.name)

    def generate(self):
        out = "!{} = !{".format(self.name)
        out += "i32 {}, !\"{}\", {} {}}".format(self.type.value, self.id, self.value.str_ty(), self.value.str_rep())
        return out

class ir_global_metadata:
    #!<name> = !{!"<id>"}
    def __init__(self, name: str, id: str) -> None:
        self.name: str = name
        self.id: str = id

    def str_rep(self):
        return "!{}".format(self.name)

    def generate(self):
        out = "!{} = !{".format(self.name)
        out += "!\"{}\"}".format(self.type.value, self.id, self.value.str_ty(), self.value.str_rep())
        return out
    
#IR_FUNCTION
class ir_function: 
    def __init__(self, return_var: ir_fnc_var, function_name: str, linkage:linkage_types = None, preemption_specifier: preemption_specifier_types = None, visability : visability_types = None, dll_storage_class: dll_storage_types = None, cconv: calling_conventions_types = None, argument_list: list = [], unnamed_local: unnamed_local_type = None, addr_space: int = None, function_attribs: list = [], section: str = None, comdat: comdat_types = None, align: int = None, gc: str = None, prefix: ir_val = None, prologue: None = None, personality: bool = None, meta_data: str = None):
        self.linkage:linkage_types = linkage
        self.preemption_specifier: preemption_specifier_types = preemption_specifier
        self.visability : visability_types = visability
        self.dll_storage_class: dll_storage_types = dll_storage_class
        self.cconv: calling_conventions_types = cconv
        self.return_var: ir_fnc_var = return_var           #Name of parameter is gonna be ignored!
        self.function_name: str = function_name
        self.argument_list: list[ir_var] = argument_list
        self.unnamed_local: unnamed_local_type = unnamed_local
        self.addr_space: int = addr_space
        self.function_attribs: list[function_attribute_types] = function_attribs
        self.section: str = section
        self.comdat: comdat_types = comdat
        self.align: int = align
        self.gc: str = gc
        self.prefix: ir_val = prefix
        self.prologue: None = prologue #NOT SUPPOTED FOR NOW
        self.personality: bool = personality
        self.meta_data: str = meta_data
        self.basic_blocks: list[ir_basic_block] = []
    
    def add_basic_block(self, basic_block: ir_basic_block):
        self.basic_blocks.append(basic_block)

    def generate(self):
        out = "define {}{}{}{}{}{} @{}(".format(opt(self.linkage), opt(self.preemption_specifier), opt(self.visability), opt(self.dll_storage_class), opt(self.cconv), self.return_var.str_ty(), self.function_name)
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

#IR_FILE

class ir_file_target_triple:
    def __init__(self, architecture: target_tripple_architecture_type, vendor: target_tripple_vendor_type, operating_system: target_tripple_operating_system_type) -> None:
        self.architecture: target_tripple_architecture_type = architecture
        self.vendor: target_tripple_vendor_type = vendor
        self.operating_system: target_tripple_operating_system_type = operating_system

    def generate(self):
        return "target triple = \"{}-{}-{}\"".format(self.architecture.value, self.vendor.value, self.operating_system.value)

class ir_file_target_datalayout:
    def __init__(self, little_endian: bool = None, stack_align: int = None, mem_addr_space: target_datalayout_addr_space = None, glob_var_addr_space: target_datalayout_addr_space = None, obj_addr_space: target_datalayout_addr_space = None, ptr_align: list = [], int_align: list = [], vector_align: list = [], float_align: list = [], obj_align: list = [], fnc_align: list = [], mangling: target_datalayout_mangling_type = None, native_int_widths: target_datalayout_addr_space = None, ptr_addr_space: list = []) -> None:
        self.little_endian: bool = little_endian
        self.stack_align: int = stack_align
        self.mem_addr_space: target_datalayout_addr_space = mem_addr_space
        self.glob_var_addr_space: target_datalayout_addr_space = glob_var_addr_space
        self.obj_addr_space: target_datalayout_addr_space = obj_addr_space
        self.ptr_align: list[target_datalayout_ptr_align] = ptr_align
        self.int_align: list[target_datalayout_int_align] = int_align
        self.vector_align: list[target_datalayout_vector_align] = vector_align
        self.float_align: list[target_datalayout_float_align] = float_align
        self.obj_align: list[target_datalayout_obj_align] = obj_align
        self.fnc_align: list[target_datalayout_fnc_align] = fnc_align
        self.mangling: target_datalayout_mangling_type = mangling
        self.native_int_widths: target_datalayout_addr_space = native_int_widths
        self.ptr_addr_space: list[target_datalayout_addr_space] = ptr_addr_space #NOT SUPPORTED
        if self.ptr_addr_space:
            print("ATTENTION - ptr_addr_space it not supported for now!")
    
    def add_endianess(self, little_endian: bool):
        self.little_endian: bool = little_endian

    def add_stack_align(self, align: int):
        self.stack_align: int = align

    def add_mem_addr_space(self, int_values: list):
        self.mem_addr_space: target_datalayout_addr_space = target_datalayout_addr_space(int_values)

    def add_glob_var_addr_space(self, int_values: list):
        self.glob_var_addr_space: target_datalayout_addr_space = target_datalayout_addr_space(int_values)
    
    def add_obj_addr_space(self, int_values: list):
        self.obj_addr_space: target_datalayout_addr_space = target_datalayout_addr_space(int_values)

    def add_ptr_align_obj(self, ptr_align: target_datalayout_ptr_align):
        self.ptr_align.append(ptr_align)
    
    def add_ptr_align(self, size: int, abi: int, pref: int = None):
        self.ptr_align.append(target_datalayout_ptr_align(size, abi, pref))
        
    def add_int_align_obj(self, int_align: target_datalayout_int_align):
        self.int_align.append(int_align)

    def add_int_align(self, size: int, abi: int, pref: int = None):
        self.int_align.append(target_datalayout_int_align(size, abi, pref))
    
    def add_vector_align_obj(self, vector_align: target_datalayout_vector_align):
        self.vector_align.append(vector_align)
    
    def add_vector_align(self, size: int, abi: int, pref: int = None):
        self.vector_align.append(target_datalayout_vector_align(size, abi, pref))
    
    def add_float_align_obj(self, float_align: target_datalayout_float_align):
        self.float_align.append(float_align)

    def add_float_align(self, size: int, abi: int, pref: int = None):
        self.float_align.append(target_datalayout_float_align(size, abi, pref))
    
    def add_obj_align_obj(self, obj_align: target_datalayout_obj_align):
        self.obj_align.append(obj_align)
    
    def add_obj_align(self, abi: int, pref: int = None):
        self.obj_align.append(target_datalayout_obj_align(abi, pref))

    def add_fnc_align_obj(self, fnc_align: target_datalayout_fnc_align):
        self.fnc_align.append(fnc_align)

    def add_fnc_align(self, type: str, abi: int):
        self.fnc_align.append(target_datalayout_fnc_align(type, abi))

    def add_mangling(self, mangling_type: target_datalayout_mangling_type):
        self.mangling: target_datalayout_mangling_type = target_datalayout_mangling_type(mangling_type)

    def add_native_int_widths(self, int_values: list):
        self.native_int_widths: target_datalayout_addr_space = target_datalayout_addr_space(int_values)

    def generate(self):
        tmp_arr = []
        if self.little_endian:
            if self.little_endian is False:
                tmp_arr.append("E")
            else:
                tmp_arr.append("e")
        if self.mangling:
            tmp_arr.append("m:{}".format(self.mangling.value))
        for a in self.fnc_align:
            tmp_arr.append(a.generate())
        for a in self.obj_align:
            tmp_arr.append(a.generate())
        for a in self.float_align:
            tmp_arr.append(a.generate())
        for a in self.vector_align:
            tmp_arr.append(a.generate())
        for a in self.int_align:
            tmp_arr.append(a.generate())
        for a in self.ptr_align:
            tmp_arr.append(a.generate())
        if self.obj_addr_space:
            tmp_arr.append("A{}".format(self.obj_addr_space.generate()))
        if self.glob_var_addr_space:
            tmp_arr.append("G{}".format(self.glob_var_addr_space.generate()))
        if self.mem_addr_space:
            tmp_arr.append("P{}".format(self.mem_addr_space.generate()))
        if self.stack_align:
            tmp_arr.append("S{}".format(self.stack_align))
        
        out = "target datalayout = \""
        for i, e in enumerate(tmp_arr):
            if i == 0:
                out += e
            else:
                out += "-{}".format(e)
        return out + "\""
        
class ir_file:
    def __init__(self, source_filename: str = None, target_datalayout: ir_file_target_datalayout = None, target_triple: ir_file_target_triple = None) -> None:
        self.source_filename: str = source_filename
        
        #Target_Datalayout
        self.target_datalayout:  ir_file_target_datalayout = target_datalayout

        #Target_Tripple
        #<ARCHITECTURE> - <VENDOR> - <OPERATING_SYSTEM>
        self.target_triple: ir_file_target_triple = target_triple

        # CONTENT --------
        #->Declarations
        self.glob_var_declarations: list[irbb_global_declare_variable] = []
        self.glob_fnc_declarations: list[irbb_global_declare_function] = []

        #->Functions
        self.glob_fnc: list[ir_function] = []

        #->Attributes
        self.glob_attribs_fnc: list[ir_global_attribs_function] = []
        self.glob_attribs_param: list[ir_global_attribs_parameter] = []

        self.glob_metadata_module_flags: list[ir_global_metadata_module_flags] = []
        self.glob_metadata_ident: list[ir_global_metadata] = []


    def set_source_filename(self, source_filename: str):
        self.source_filename: str = source_filename

    def set_target_datalayout(self, target_datalayout: ir_file_target_datalayout):
        self.target_datalayout: ir_file_target_datalayout = target_datalayout

    def set_target_tripple(self, target_triple: ir_file_target_triple):
        self.target_triple: ir_file_target_triple = target_triple

    def add_glob_var_declaration(self, glob_var_declaration: irbb_global_declare_variable):
        self.glob_var_declarations.append(glob_var_declaration)
    
    def add_glob_fnc_declaration(self, glob_fnc_declaration: irbb_global_declare_function):
        self.glob_fnc_declarations.append(glob_fnc_declaration)
    
    def add_glob_fnc(self, glob_fnc: ir_function):
        self.glob_fnc.append(glob_fnc)
    
    def add_glob_attribs_fnc(self, glob_attribs_fnc: ir_global_attribs_function):
        self.glob_attribs_fnc.append(glob_attribs_fnc)
    
    def add_glob_attribs_param(self, glob_attribs_param: ir_global_attribs_parameter):
        self.glob_attribs_param.append(glob_attribs_param)
    
    def add_glob_metadata_module_flags(self, glob_metadata_module_flags: ir_global_metadata_module_flags):
        self.glob_metadata_module_flags.append(glob_metadata_module_flags)

    def add_glob_metadata_ident(self, glob_metadata_ident: ir_global_metadata):
        self.glob_metadata_ident.append(glob_metadata_ident)

    def generate(self):
        def nl(txt: str = None):
            if txt:
                return "{}\n".format(txt)
            else:
                return "\n"
        out = ""

        #Source_filename
        if self.source_filename:
            out += nl("source_filename = \"{}\"".format(self.source_filename))
        #target_datalayout
        if self.target_datalayout:
            out += nl(self.target_datalayout.generate())
        #target_triple
        if self.target_triple:
            out += nl(self.target_triple.generate())
        
        if self.source_filename or self.target_datalayout or self.target_triple:
            out += nl()

        #global variables
        if self.glob_var_declarations:
            for gv in self.glob_var_declarations:
                out += nl(gv.generate())
            out += nl()
        
        #functions
        if self.glob_fnc:
            for fnc in self.glob_fnc:
                out += nl(fnc.generate())

        #function declarations
        if self.glob_fnc_declarations:
            for gf in self.glob_fnc_declarations:
                out += nl(gf.generate())

        
        #Function attributes:
        if self.glob_attribs_fnc:
            for fa in self.glob_attribs_fnc:
                out += nl(fa.generate())
        #Parameter attributes:
        if self.glob_attribs_param:
            for pa in self.glob_attribs_param:
                out += nl(pa.generate())
        
        if self.glob_attribs_fnc or self.glob_attribs_param:
            out += nl()

        #llvm module flags
        if self.glob_metadata_module_flags:
            tmp = "!llvm.module.flags = !{"
            for i, md in enumerate(self.glob_metadata_module_flags):
                if i != 0:
                    tmp += ", "
                tmp += md.str_rep()
            tmp += "}"
            out += nl(tmp)

        #llvm mident
        if self.glob_metadata_ident:
            tmp = "!llvm.ident = !{"
            for i, md in enumerate(self.glob_metadata_ident):
                if i != 0:
                    tmp += ", "
                tmp += md.str_rep()
            tmp += "}"
            out += nl(tmp)

        if self.glob_metadata_module_flags or self.glob_metadata_ident:
            out += nl()

        #Metadata
        for mmd in self.glob_metadata_module_flags:
            out += nl(mmd.generate())

        for imd in self.glob_metadata_ident:
            out += nl(imd.generate())
        
        return out


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
    def __init__(self, old_var: ir_val, operation: atomicrmw_op_type, pointer: ir_var, value: ir_val, ordering: atomic_memory_ordering_constraints_type, volatile: bool = False, syncscope: str = None, align: int = None) -> None:
        super().__init__()
        self.old_var: ir_var = old_var
        self.operation: atomicrmw_op_type = operation
        self.pointer: ir_var = pointer
        self.value: ir_val = value
        self.ordering: atomic_memory_ordering_constraints_type = ordering
        self.volatile: bool = volatile
        self.syncscope: str = syncscope
        self.align: int = align
    
    def generate(self):
        out = "{} = atomicrmw".format(self.old_var.str_rep())
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
        if len(self.operand_bundle) != 0:
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
            if i != 0:
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



""" EXAMPLE
file = ir_file("test_file.c")
file.set_target_tripple(ir_file_target_triple(target_tripple_architecture_type.arm64, target_tripple_vendor_type.apple, target_tripple_operating_system_type.macosx11_0_0))

tl = ir_file_target_datalayout(True, 128)
tl.add_mangling(target_datalayout_mangling_type.macho)
tl.add_int_align(64, 64)
tl.add_int_align(128, 128)
tl.add_native_int_widths([32, 64])
tl.add_stack_align(128)

file.set_target_datalayout(tl)

x = ir_function(ir_var(ir_dtype.i32), "testFunction")
x.add_basic_block(irbb_alloca(ir_var(ir_dtype.i64, "t0"), 4))
x.add_basic_block(irbb_alloca(ir_var(ir_dtype.float, "t1"), 4))
x.add_basic_block(irbb_store(ir_var(ir_dtype.i32, "ab"), ir_var(ir_dtype.i64, "cd"), 4))
x.add_basic_block(irbb_load(ir_var(ir_dtype.i32, "cc"), ir_var(ir_dtype.i32, "bb"), 4))
x.add_basic_block(irbb_add(ir_var(ir_dtype.i32, "o"), ir_var(ir_dtype.i32, "l"), ir_var(ir_dtype.i32, "p"), True))
x.add_basic_block(irbb_fadd(ir_var(ir_dtype.float, "j"), ir_var(ir_dtype.float, "n"), ir_val(ir_dtype.float, "4.0"), [fast_math_flags_type.nnan, fast_math_flags_type.afn]))
x.add_basic_block(irbb_atomicrmw(ir_var(ir_dtype.i32, "old"), atomicrmw_op_type._add, ir_var(ir_dtype.i32, "k"), ir_val(ir_dtype.i32, "5"), atomic_memory_ordering_constraints_type.acquire, True, "test", 3))
x.add_basic_block(irbb_call(ir_var(ir_dtype.i32, "2"), "add4", [ir_var(ir_dtype.i16, "a"), ir_var(ir_dtype.float, "b")], tail_type._musttail, [], calling_conventions_types.cc_10, [], 4, [], []))
x.add_basic_block(irbb_return())

y = ir_function(ir_var(ir_dtype.i32), "testFunction")
y.add_basic_block(irbb_alloca(ir_var(ir_dtype.i64, "t0"), 4))
y.add_basic_block(irbb_alloca(ir_var(ir_dtype.float, "t1"), 4))
y.add_basic_block(irbb_load(ir_var(ir_dtype.i32, "cc"), ir_var(ir_dtype.i32, "bb"), 4))
y.add_basic_block(irbb_atomicrmw(ir_var(ir_dtype.i32, "old"), atomicrmw_op_type._add, ir_var(ir_dtype.i32, "k"), ir_val(ir_dtype.i32, "5"), atomic_memory_ordering_constraints_type.acquire, True, "test", 3))
y.add_basic_block(irbb_call(ir_var(ir_dtype.i32, "2"), "add4", [ir_var(ir_dtype.i16, "a"), ir_var(ir_dtype.float, "b")], tail_type._musttail, [], calling_conventions_types.cc_10, [], 4, [], []))
y.add_basic_block(irbb_return())

file.add_glob_fnc(x)
file.add_glob_fnc(y)

print(file.generate())
"""