import math
def solution(n, k):
    nums = list(range(1,n+1))
    k -=1
    res =[]
    while n>0:
        n-=1
        fact = math.factorial(n)
        index = k // fact
        res.append(nums.pop(index))
        k %= fact
    return res