def solution(str1, str2):
    answer = 0
    intersection = 0
    union  =0
    str1 = str1.lower()
    str2 = str2.lower()
    def get_substring(s):
        substrings = []
        for i in range(len(s)-1):
            substring = s[i:i+2]
            if substring.isalpha():
                substrings.append(substring)
        return substrings
    arr1 = get_substring(str1)
    arr2 = get_substring(str2)
    
    for s in arr1:
        if s in arr2:
            intersection += 1
            arr2.remove(s) 
        union += 1 
    for s in arr2:
        union += 1
        
    if intersection==0 and union ==0 :
        return 1*65536
    elif intersection==0 and union !=0:
        return 0
    else:
        return int((intersection/union)*65536)
   