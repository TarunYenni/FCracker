#!/usr/bin/python

import sys,os, time

print("############################################################################")
print("############################################################################")
print("########################### File Cracker ###################################")
print("###################### Using John / Hashcat ################################")
print("#################### Author: zZBlackArrowZz ################################")
print("############################################################################")
print("############################################################################")

file = sys.argv[1]
wordlist = sys.argv[2]

os.system("zip2john " + file + "> hash.txt")
time.sleep(2)
os.system("john hash.txt " + "-w=" + wordlist)

print(file)
print(wordlist)