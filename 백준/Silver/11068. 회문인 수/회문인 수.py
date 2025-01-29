import sys
input = sys.stdin.readline
def to_base(s, b):
    res = []
    while s > 0:
        res.append(s%b)
        s //= b
    return res[::-1]

def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i]!=s[-1-i]:
            return False
    return True

t = int(input())
for _ in range(t):
    n= int(input())
    found = False
    for b in range(2, 65):
        if is_palindrome(to_base(n, b)):
            found = True
            break
    print(1 if found else 0)