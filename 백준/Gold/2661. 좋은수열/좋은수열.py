import sys
input = sys.stdin.readline

n = int(input())

def is_good(s):
    length = len(s)
    for k in range(1, length // 2 + 1):
        if s[-k:] == s[-2*k:-k]:
            return False
    return True

def dfs(s):
    if len(s) == n:
        print(s)
        exit(0)
    for ch in '123':
        if is_good(s + ch):
            dfs(s + ch)

dfs("")