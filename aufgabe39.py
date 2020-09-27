"""
Write a Python program to list all files in a directory in Python.
this app will not working if u don't have student file
"""
from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
print(files_list);
