

from os import PRIO_USER
from readline import insert_text


def output (line, testType, index):
    index +=1
    print("["+testType+"] test faild")
    if testType == "magic number":
        pass
    if testType == "magic string":
        pass
    if testType == "attribute":
        pass
    if testType == "unreachable":
        pass
    if testType == "parameters":
        print("there is more than 3 parameters in line number: "+ index + "\nline")
        pass

