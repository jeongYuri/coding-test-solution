import sys
input = sys.stdin.readline

def findnum(n):
    for i in range(max(1,n-54),n):
        allsum = i+ sum(map(int, str(i)))
        if allsum ==n:
            return i
    return 0
n = int(input())
result = findnum(n)
print(result)