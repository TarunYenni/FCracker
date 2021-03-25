#!/usr/bin/python

import sys, os, time
import argparse


# ssh2john
print("############################################################################")
print("############################################################################")
print("########################### File Cracker ###################################")
print("###################### Using John / Hashcat ################################")
print("#################### Author: zZBlackArrowZz ################################")
print("############################################################################")
print("############################################################################")
print("################### Currently in development ###############################")
print("\n")
parser = argparse.ArgumentParser()

parser.add_argument("-f","--ifile", metavar="<Input_File>", required=True, help="Take's a file_name as input")
parser.add_argument("-w","--wordlist", metavar="<wordlist>", required=True, help="Take's a wordlist as input")

args = parser.parse_args()

#global file_name
file_name = args.ifile
wordlist = args.wordlist

def crack_hash(wordlist):
    os.system("john hash.txt " + "-w=" + wordlist)

def create_hash(file_name):
    if ".zip" in file_name:
        os.system("zip2john " + file_name + "> hash.txt")
    elif ".pdf" in  file_name:
        os.system("programs/pdf2john.pl "+ file_name +"> hash.txt")
    elif ".rar" in file_name:
        os.system("rar2john "+ file_name + "> hash.txt")
    elif (".doc" or ".docx") in file_name:
        os.system("programs/office2john.py "+ file_name +">hash.txt")
    elif ".7z" in file_name:
        os.system("programs/7z2john.pl "+ file_name +"> hash.txt")
    else:
        print("File Format not supported!!!")

create_hash(file_name)
crack_hash(wordlist)
