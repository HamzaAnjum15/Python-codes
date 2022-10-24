# Write a Python program to list all files in a directory in Python.
from os import listdir
from os.path import isfile, join
file_list=[f for f in listdir('/Users/dell/Desktop') if isfile(join('/Users/dell/Desktop',f))]
print(file_list);


