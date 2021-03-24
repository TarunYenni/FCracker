#!/usr/bin/python

import sys, os, time

grade = sys.argv[1]

def print_grade(grade):
    if ".txt" in grade:
        print("A")
    elif ".zip" in  grade:
        print("B")
    else:
        print("No Grade")
print_grade(grade)
