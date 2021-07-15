import subprocess
import os.path
from log import log

filename = "tmp/prog"

def decompile_without_hex_rep(filename):
    p = subprocess.Popen(["objdump", "-D", "--no-show-raw-insn", filename], stdout=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode("utf-8")
    f = open("tmp/tmp.asm", "w")
    f.write(out)
    f.close()

def decompile(filename):
    if os.path.isfile(filename):
        subp_command = ["objdump", "-D", filename]
        p = subprocess.Popen(subp_command, stdout=subprocess.PIPE)
        print()
        out, err = p.communicate()
        out = out.decode("utf-8")
        f = open("tmp/tmp.asm", "w")
        f.write(out)
        f.close()
        log(os.path.basename(__file__), "{} decompiled sucessfully".format(filename))
    else:
        log(os.path.basename(__file__), "File not found: {}".format(filename))
    

def getHEX(startAddress, stopAddress):
    """Converting the given mach-o executeable and returns the section between start- and stop-address

    Args:
        startAddress (String): Start-address as hex-value
        stopAddress ([type]): Stop-address as hex-value
    """
    p = subprocess.Popen(["objdump", "-D", "--no-show-raw-insn", filename], stdout=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode("utf-8")
    f = open("tmp/tmp.asm", "w")
    f.write(out)
    f.close()

decompile(filename)