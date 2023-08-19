def solution(myString):
    parts = myString.split("x")  
    parts = [i for i in parts if i != ""]  
    parts.sort()  
    return parts
