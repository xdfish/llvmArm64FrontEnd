import parser
import irgen

asm = parser.parseASM()

curFunction = ""
for inst in asm:
    if inst.function != curFunction:
        irgen.
    
