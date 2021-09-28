from os import strerror
import subprocess
import os.path
from log import log


#Only for Development
def decompile_without_hex_rep(filename: str, export: bool) -> any:
    """
    Disasembles an executeable to an assember listing without the hex representation of the Instructions
    This function is currently not in use for the ztransofmration process.

    :param filename: filename (and path) to the file
    :type filename: str
    :param export: if True, the asm_listing ist exported to the tmp folder
    :type export: bool
    :return: returns an assembler Listing if successful, or False in case of an error.
    :rtype: str or Bool(False)
    """
    if os.path.isfile(filename):
        p = subprocess.Popen(["objdump", "-D", "--no-show-raw-insn", filename], stdout=subprocess.PIPE)
        out, err = p.communicate()
        out = out.decode("utf-8")
        if export:
            f = open("tmp/tmp_wh.asm", "w")
            f.write(out)
            f.close()
        log(os.path.basename(__file__), "{} decompiled sucessfully without hex representation".format(filename))
        return out
    else:
        log(os.path.basename(__file__), "File not found: {}".format(filename))
        return False
#Only for Development
def decompile(filename, export):
    """
    Disasembles an executeable to an assembler listing with the hex-representation of the instructions

    :param filename: filename (and path) to the file
    :type filename: str
    :param export: if True, the asm_listing ist exported to the tmp folder
    :type export: bool
    :return: returns an assembler Listing if successful, or False in case of an error.
    :rtype: str or Bool(False)
    """
    if os.path.isfile(filename):
        subp_command = ["objdump", "-D", filename]
        p = subprocess.Popen(subp_command, stdout=subprocess.PIPE)
        out, err = p.communicate()
        out = out.decode("utf-8")
        if export:
            f = open("../tmp/tmp.asm", "w")
            f.write(out)
            f.close()
        log(os.path.basename(__file__), "{} decompiled sucessfully".format(filename))
        return out
    else:
        log(os.path.basename(__file__), "File not found: {}".format(filename))
        return False


##LIVE <-
class disasembled_raw():
    def __init__(self, source_filename: str = None, export_files: bool = False) -> None:
        self.filename: str = source_filename
        self.private_header: str = None
        self.text_section: str = None
        self.cstring_section: str = None
        self.symbol_table: str = None
        self.export_files: bool = export_files
        if not os.path.isfile(self.filename):
            log(os.path.basename(__file__), "File not found: {}".format(source_filename))

    def get_text_section(self):
        subp_command = ["objdump", "-D", self.filename, "--macho", "--full-leading-addr", "--no-symbolic-operands"]
        p = subprocess.Popen(subp_command, stdout=subprocess.PIPE)
        out, err = p.communicate()
        out = out.decode("utf-8")
        self.text_section = out.splitlines()
        if self.export_files:
            export_file(self.filename, out, "_str_section")
        log(os.path.basename(__file__), "-> str_section (DONE)")
        

    def get_private_header(self):
        subp_command = ["objdump", "-C", self.filename, "--macho", "--private-header"]
        p = subprocess.Popen(subp_command, stdout=subprocess.PIPE)
        out, err = p.communicate()
        out = out.decode("utf-8")
        self.private_header = out.splitlines()
        if self.export_files:
            export_file(self.filename, out, "_private_header")
        log(os.path.basename(__file__), "-> private_header (DONE)")

    def get_cstring_section(self):
        subp_command = ["objdump", "-C", self.filename, "--macho", "--section=__cstring"]
        p = subprocess.Popen(subp_command, stdout=subprocess.PIPE)
        out, err = p.communicate()
        out = out.decode("utf-8")
        self.cstring_section = out.splitlines()
        if self.export_files:
            export_file(self.filename, out, "_cstring_section")
        log(os.path.basename(__file__), "-> cstring_section (DONE")

    def get_symbol_table(self):
        subp_command = ["objdump", "-C", self.filename, "--macho", "--indirect-symbols"]
        p = subprocess.Popen(subp_command, stdout=subprocess.PIPE)
        out, err = p.communicate()
        out = out.decode("utf-8")
        self.symbol_table = out.splitlines()
        if self.export_files:
            export_file(self.filename, out, "indirect_symbols")
        log(os.path.basename(__file__), "-> symbol_table (DONE)")

    def disasemble(self):
        log(os.path.basename(__file__), "Disasembling file: {}".format(self.filename))
        self.get_text_section()
        self.get_private_header()
        self.get_cstring_section()
        self.get_symbol_table()
        log(os.path.basename(__file__), "COMPLETE\n")
        return self


#Helpfunctions
def export_file(filename: str, content: str, filename_suffix: str = ""):
    f = open("../tmp/{}{}.asm".format(filename.split("/")[-1], filename_suffix), "w")
    f.write(content)
    f.close()
    return True
