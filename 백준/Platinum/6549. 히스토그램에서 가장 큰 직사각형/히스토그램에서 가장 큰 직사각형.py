import sys
input = sys.stdin.readline

def histogram(n,hist):
    stack = []
    ans = 0
    hist.append(0)
    for i in range(n+1):
        v = hist[i]
        start = i
        while stack and stack[-1][1]>=v:
            start, height = stack.pop()
            ans = max(ans, (i-start)*height)
        stack.append([start,v])
    print(ans)
while(True):
    nums = list(map(int,input().split()))
    n = nums[0]
    if n==0:
        break
    histogram(n, nums[1:])




