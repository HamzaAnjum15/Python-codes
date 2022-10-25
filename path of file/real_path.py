# Write a python program to get the path and name of the file that is currently executing.
import os
print("the current file is: ",os.path.realpath(__file__))