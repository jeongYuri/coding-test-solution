import sys
input = sys.stdin.readline
t = int(input())
arr = []
ans = {}
for _ in range(t):
    x = input().strip().split('.')
    arr.append(x[1])
for i in arr:
    if i not in ans:
        ans[i] = 1
    else:
        ans[i]+=1
sorted_key = sorted(ans.keys())
for key in sorted_key:
    value = ans[key]
    print(f"{key} {value}")