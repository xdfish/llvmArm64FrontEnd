from enum import Enum

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
    any = "comdat any"
    exactmatch = "comdat exactmatch"
    largest = "comdat largest"
    nodeduplicate = "comdat nodeduplicate"
    samesize = "comdat samesize"
