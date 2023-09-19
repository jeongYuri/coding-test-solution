def solution(s):
    count = 0
    for start in range(len(s)):
        rotation = s[start:]+s[:start]
        while True:
            length= len(rotation)
            rotation = rotation.replace("[]","")
            rotation = rotation.replace("()","")
            rotation = rotation.replace("{}","")
            if len(rotation)==0:
                count +=1
                break
            if length==len(rotation):
                break
    return count