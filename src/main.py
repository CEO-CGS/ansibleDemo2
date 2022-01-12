#!/usr/bin/python

from github import Github
import sys

print(sys.argv[1])
print("hello")

my_file = open("file.txt", "w")
#Open file for writing

my_file.write("First Line\n")

my_file.close()

with open('file.txt') as f:
    contents = f.read()
    print(contents)
print("Hello World)
    input ("How are you?")
    input = yes 
