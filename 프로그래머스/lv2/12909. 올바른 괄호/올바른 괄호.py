def solution(s):
    stac=[]
    for i in s:      
        if len(stac)==0:
            if i=="(":
                stac.append(i)
            else:
                return False
        elif i==")":
            stac.pop() 
        elif i=="(":
            stac.append(i)
            
    return True if len(stac)==0 else False