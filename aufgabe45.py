"""
Write a Python program to list all files in a directory in Python.
"""from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/x/students') if isfile(join('/home/x/students', f))]
print(files_list);
