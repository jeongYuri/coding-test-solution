import math
def gcd(arr):
    g = arr[0]
    for x in arr[1:]:
        g = math.gcd(g,x)
    return g
def check(g,arr):
    for x in arr:
        if x%g==0:
            return False
    return True
def solution(arrayA, arrayB):
    ans = 0
    ga = gcd(arrayA)
    gb = gcd(arrayB)
    if check(ga, arrayB):
        ans = max(ans, ga)
    if check(gb, arrayA):
        ans = max(ans,gb)
    return ans