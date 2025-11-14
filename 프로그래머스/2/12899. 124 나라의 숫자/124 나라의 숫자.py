def solution(n):
    answer = ''
    ans = ['1','2','4']
    while n>0:
        n = n-1
        answer = ans[n%3]+answer
        n//=3
    return answer