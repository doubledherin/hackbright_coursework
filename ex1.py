"""
Your job is to write a program, ex1.py, that does the following things:

Create 26 directories in the current directory, one for each letter of the alphabet: 
./a/ ./b/ ./c/ etc.

Loop through all the files in the original_files directory, and organize each of 
those files into the directory that their name starts with.
"""

import string, shutil, os, os.path

current = os.getcwd()
path_to_original = os.path.relpath("/original_files", current)
print current
print path_to_original

os.chdir("./original_files/")
newcurrent = os.getcwd()
print newcurrent

dirs = os.listdir("./")
print dirs

#for char in string.ascii_lowercase:
#	os.mkdir(char)



