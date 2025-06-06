def solution(s):
    answer = len(s)
    
    for step in range(1,len(s)//2+1):
        compressed = ''
        prev = s[:step] #step 만큼 쪼개면서 가야지...
        cnt = 1
        
        for i in range(step, len(s),step):
            if s[i:i+step]==prev:
                cnt +=1
            else:
                compressed += str(cnt)+prev if cnt>1 else prev
                prev = s[i:i+step]
                cnt =1
        compressed += str(cnt) + prev if cnt>1 else prev
        answer = min(answer, len(compressed))
    return answer