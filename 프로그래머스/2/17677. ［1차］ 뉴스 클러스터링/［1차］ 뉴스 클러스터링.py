from collections import Counter
def solution(str1, str2):
    answer = 0
    arr1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    arr2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    cntarr1 = Counter(arr1)
    cntarr2 = Counter(arr2)
    
    inter = cntarr1 & cntarr2
    union = cntarr1 | cntarr2
    
    len_inter = sum(inter.values())
    len_union = sum(union.values())
    
    if len_union == 0:
        return 65536

    ans = int((len_inter/len_union)*65536)
    return ans