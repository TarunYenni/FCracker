#!/usr/bin/python

import sys, os, time

#file_name = sys.argv[1]
#print(file_name)
#def createhash(file_name):
#    if ".zip" in (file_name):
#        os.system("zip2john " + file_name + "> hash.txt")
#    elif ".pdf" in (file_name):
#        os.system(file_name)
#    else:
#        print("File Not Found")
#    return

#createhash(file_name)
# ssh2john


#global file_name
file_name = sys.argv[1]
wordlist = sys.argv[2]

def crack_hash(wordlist):
    os.system("john hash.txt " + "-w=" + wordlist)


def create_hash(file_name):
    if ".zip" in file_name:
        os.system("zip2john " + file_name + "> hash.txt")
    elif ".pdf" in  file_name:
        print("PDF")
    elif ".rar" in file_name:
        print("RAR")
    elif (".doc" or ".docx") in file_name:
        print("DOC")
    elif ".7z" in file_name:
        print("7z")
    else:
        print("File Format not supported!!!")
create_hash(file_name)
crack_hash(wordlist)
