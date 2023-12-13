def GCD(a,b):
    while(b):
        a,b = b,a%b
    return a
def LCM(a,b):
    result = (a*b)//GCD(a,b)
    return result

a, b = map(int, input().split())
print(GCD(a,b))
print(LCM(a,b))