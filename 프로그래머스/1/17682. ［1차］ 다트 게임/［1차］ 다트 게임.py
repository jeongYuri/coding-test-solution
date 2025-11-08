def solution(dartResult):
    scores = []
    i = 0
    
    while i<len(dartResult):
        if dartResult[i]=='1' and i+1<len(dartResult) and dartResult[i+1]=='0':
            score = 10
            i+=2
        else:
            score = int(dartResult[i])
            i+=1
        if dartResult[i]=='S':
            score **=1
        elif dartResult[i]=='D':
            score **=2
        elif dartResult[i]=='T':
            score**=3
        i+=1
        if i<len(dartResult) and dartResult[i] in ['#','*']:
            if dartResult[i]=='*':
                score *=2
                if scores:
                    scores[-1]*=2
            elif dartResult[i]=='#':
                score *=-1
            i+=1
        scores.append(score)
    return sum(scores)
            
    return answer