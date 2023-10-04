def solution(n, t, m, p):
    answer ="0"
    rotation ='0123456789ABCDEF'
    for num in range(1,t*m):
        result = ""
        while num>0:
            num, r = divmod(num,n)
            result += rotation[r]
        answer+=result[::-1]
    return answer[p-1::m][:t]