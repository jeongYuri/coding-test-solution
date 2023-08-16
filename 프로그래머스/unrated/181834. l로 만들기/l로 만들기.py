import re
def solution(myString):
    myString = re.sub("(a|b|c|d|e|f|g|h|i|j|k)","l",myString)
    return myString