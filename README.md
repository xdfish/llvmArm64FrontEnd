# llvmArm64FrontEnd
This tool converts arm64 mac executeables (mach-o) to llvm-IR (intermediate Representation, .ll) files.

<h1>Quickstart</h1>
1. use the following command for start the transformation process for an arm mach-o executeable:
	$ python3 llvmArm64FrontEnd.py <executeable_file>

2. your done :)


<h1> Startarguments </h1>
$ llvmArm64FrontEnd [ --version | --help ]

	--version	    - Display the version of this program
	--help		    - Display available options

$ llvmArm64FrontEnd <input_name> [-o <output_name>][-d 0..3] [-x]

	-o <file>	    - Write output to <file>
	-d [0..3]	    - Set the level of detail of the displayed informations
	-x 		        - Enable output of not transformed assembler instructions
  
  
