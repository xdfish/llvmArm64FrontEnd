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