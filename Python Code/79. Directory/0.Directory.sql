#                                  Directory

os module – This module is used to perform simple operation on directories. This module represents operating system dependent functionality.
import os


getcwd() – This method is used to know the currently working directory.
	Syntax:- os.getcwd()

mkdir(‘dirname’) – This method is used to create a directory in the present directory. 
	Syntax:- os.mkdir(‘dirname’)

mkdir(‘parentdirname/childdirname’) – This method is used to create a child directory in the parent directory. Parent directory must be exist else it will show error.
	Syntax:- os.mkdir(‘parentdirname/childdirname’)


makedirs(‘parentdir/childdir/grandchilddir’) – This method is used to recursively create sub directories. 
	Syntax:- os.makedirs(‘parentdir/childdir/grandchilddir’)

chdir(‘dirname’) – This method is used to change current working directory.
	Syntax:- os.chdir(‘dirname’)

rename(‘oldname’, ‘newname’) – This method is used to change the directory name.
	Syntax:- os.rename(‘oldname’, ‘newname’)


rmdir(‘dirname’) – This method is used to remove a directory from the current working directory. We can also specify path for directory. 
	Syntax:- os.rmdir(‘dirname’), os.rmdir(‘parentdirname/childdirname’)

removedirs(‘dirname’) – This method is used to recursively remove all directories. 
	Syntax:- os.removedirs(‘parentdirname/childdirname’)

walk() – This method is used to know contents of a directory including sub directory. It returns an iterator object whose contents can be displayed using for loop. This iterator object contains directory path, directoryname, filename found in the specified directory.


Syntax:- os.walk(path, topdown=True, onerror=None, followlinks=False)
path – It represents the directory name. we can write dot (.) to specify current directory.
topdown – If it is True the directory and its sub directories are traversed in top-down manner. If it is False then the directory and its sub directories are traversed in bottom-up manner.
onerror – It represents what to do when an error is detected. We can give a function.
followlinks – True to visit directories pointed to by symbolic links, on system that support them. If False walk() will not walk down into symbolic links that resolve to directories.
