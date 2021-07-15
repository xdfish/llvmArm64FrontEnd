import subprocess
import os.path
from log import log

#Only for Development
def decompile_without_hex_rep(filename, export):
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
    if os.path.isfile(filename):
        subp_command = ["objdump", "-D", filename]
        p = subprocess.Popen(subp_command, stdout=subprocess.PIPE)
        print()
        out, err = p.communicate()
        out = out.decode("utf-8")
        if export:
            f = open("tmp/tmp.asm", "w")
            f.write(out)
            f.close()
        log(os.path.basename(__file__), "{} decompiled sucessfully".format(filename))
        return out
    else:
        log(os.path.basename(__file__), "File not found: {}".format(filename))
        return False