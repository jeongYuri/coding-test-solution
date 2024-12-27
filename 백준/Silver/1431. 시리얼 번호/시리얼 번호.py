import sys
input = sys.stdin.readline

def sum_num(number):
    res = 0
    for i in number:
        if i.isdigit():
            res+=int(i)
    return res

n = int(input())
arr = [input().strip() for _ in range(n)]
arr.sort(key = lambda x:(len(x),sum_num(x),x))
print('\n'.join(arr))

