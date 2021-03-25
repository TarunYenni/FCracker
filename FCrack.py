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
print("Supported file formats: .zip, .rar, .pdf, .7z, .doc/.docx (2007/2013), .gpg")
parser = argparse.ArgumentParser()

parser.add_argument("-f","--ifile", metavar="<Input_File>", required=True, help="Take's a file_name as input")
parser.add_argument("-w","--wordlist", metavar="<wordlist>", help="Take's a wordlist as input")

args = parser.parse_args()


#global file_name
file_name = args.ifile
wordlist = args.wordlist

def crack_hash(wordlist):
    if args.wordlist is True:
        os.system("john hash.txt " + "-w=" + wordlist)
    else:
        os.system("john hash.txt -w=resources/wordlist/rockyou-50.txt")
    if os.path.exists("hash.txt"):
        os.system("rm hash.txt")

def create_hash(file_name):
    if ".zip" in file_name:
        os.system("zip2john " + file_name + "> hash.txt")
    elif ".pdf" in  file_name:
        os.system("resources/pdf2john.pl "+ file_name +"> hash.txt")
    elif ".rar" in file_name:
        os.system("rar2john "+ file_name + "> hash.txt")
    elif (".doc" or ".docx") in file_name:
        os.system("resources/office2john.py "+ file_name +">hash.txt")
    elif ".7z" in file_name:
        os.system("resources/7z2john.pl "+ file_name +"> hash.txt")
    elif ".gpg" in file_name:
        os.system("gpg2john "+ file_name + ">hash.txt")
    else:
        print("File Format not supported!!!")
        print("Supported File formats : .zip, .rar, .pdf, .7z, .doc/docx (2007/2013)")

create_hash(file_name)
crack_hash(wordlist)
