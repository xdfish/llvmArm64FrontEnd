import subprocess

filename = "CONVERT/prog"

def getASM(filename):
    #get ASM
    p = subprocess.Popen(["objdump", "-D", "--no-show-raw-insn", filename], stdout=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode("utf-8")
    f = open("tmp/tmp.asm", "w")
    f.write(out)
    f.close()

def getHEX(startAddress, stopAddress):
    p = subprocess.Popen(["objdump", "-D", "--no-show-raw-insn", filename], stdout=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode("utf-8")
    f = open("tmp/tmp.asm", "w")
    f.write(out)
    f.close()
    


decompile(filename)