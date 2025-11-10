def get_gcd(x,y):
    while y:
        x,y = y, x%y
    return x
def solution(arr):
    lcm = arr[0]
    for i in range(1,len(arr)):
        gcd = get_gcd(lcm, arr[i])
        lcm = lcm*arr[i]//gcd
    return lcm