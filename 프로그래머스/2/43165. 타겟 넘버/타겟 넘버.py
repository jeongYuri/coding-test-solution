answer = 0
def dfs(s,numbers,target, e):
    global answer
    n = len(numbers)
    if s==n and e ==target:
        answer+=1
        return
    if s==n:
        return
    dfs(s+1,numbers, target,e+numbers[s])
    dfs(s+1, numbers, target,e-numbers[s])
def solution(numbers, target):
    global answer
    dfs(0,numbers, target,0)
    return answer