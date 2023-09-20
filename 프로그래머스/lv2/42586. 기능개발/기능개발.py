def solution(progresses, speeds):
    result = []
    time = 0
    count = 0
    while len(progresses)!=0:
        if progresses[0]+time*speeds[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            count +=1
        else:
            if count>0:
                result.append(count)
                count = 0
            time +=1
    result.append(count)
    return result