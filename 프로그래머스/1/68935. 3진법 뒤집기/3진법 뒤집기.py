def solution(n):
    ternary = ""
    while n>0:
        n,r  = divmod(n,3)
        ternary+=str(r)
    reversed_t = ternary
    return int(reversed_t, 3)