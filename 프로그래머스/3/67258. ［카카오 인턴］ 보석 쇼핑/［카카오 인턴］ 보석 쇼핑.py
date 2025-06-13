from collections import defaultdict
def solution(gems):
    answer = []
    kind = len(set(gems)) #중복 제거하고 종류 갯수 파악
    dic = defaultdict(int)
    ans = [0,len(gems)-1] #그냥...
    start = end = 0
    dic[gems[0]] = 1
    
    while start<len(gems) and end <len(gems):
        if len(dic)<kind:
            end+=1
            if end ==len(gems):
                break
            dic[gems[end]] +=1
        else:
            if(end-start)<(ans[1]-ans[0]):
                ans = [start,end]
            dic[gems[start]]-=1
            if dic[gems[start]]==0:
                del dic[gems[start]]
            start+=1
            
                
            
        
    return [ans[0]+1, ans[1]+1]