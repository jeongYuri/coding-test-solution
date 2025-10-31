def solution(s):
    c,z = 0,0
    while s!="1":
        z+=s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]
        c += 1                    

    return [c, z]