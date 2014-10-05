"""
Your job is to write a program, ex1.py, that does the following things:

Create 26 directories in the current directory, one for each letter of the alphabet: 
./a/ ./b/ ./c/ etc.

Loop through all the files in the original_files directory, and organize each of 
those files into the directory that their name starts with.
"""

import string, shutil, os, os.path

for char in string.ascii_lowercase:
	os.mkdir(char)

# go into original files and collect filenames into 'source'
os.chdir("./original_files/")
source = os.listdir("./")

# remove hidden files from list of files 'source'
for item in source:
	if item[0] == "." or os.path.isdir(item):
		source.remove(item)

# determine first letter of filename and move it into the 
# appropriate folder
for filename in source:
	first_letter = filename[0]
	destination = os.path.abspath("../%s/" % first_letter)
	shutil.copy(filename, destination)




