def solution(array, commands):
    ans = []
    for x,y,z in commands:    
        tmp = sorted(array[x-1:y])
        ans.append(tmp[z-1])
    return ans