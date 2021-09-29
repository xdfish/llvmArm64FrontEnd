Install sphinx and the needed template by using pip3 with:
	$ pip3 install -U sphinx
	$ pip3 install sphinx-rtd-theme

Index.rst and conf.py is already modified!

1. Use the following commands to genereate a new documentation:
	
	$ make clean (to delete the old doc files)
	
2. in the current folder (sphinx) use the following commands:
	$ sphinx-apidoc -o . ..			(Generate doc for .. folder)
	$ sphinx-apidoc -o ./source ../source	(Generate doc for ../source folder)

	§ make html
