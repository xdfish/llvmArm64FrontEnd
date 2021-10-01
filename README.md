# llvmArm64FrontEnd
This tool converts arm64 mac executeables (mach-o) to llvm-IR.


$ llvmArm64FrontEnd [ --version | --help ]

	--version	    - Display the version of this program
	--help		    - Display available options

$ llvmArm64FrontEnd <input_name> [-o <output_name>][-d 0..3] [-x]

	-o <file>	    - Write output to <file>
	-d [0..3]	    - Set the level of detail of the displayed informations
	-x 		        - Enable output of not transformed assembler instructions
  
  
