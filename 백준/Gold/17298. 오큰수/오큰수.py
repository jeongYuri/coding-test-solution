from sys import stdin
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
ans = [0]*n
md = []

for i in range(n):
    while md and a[md[-1]]<a[i]:
        ans[md.pop()]=a[i]
    md.append(i)
while md:
    ans[md.pop()]=-1

result = " ".join(map(str, ans))
print(result)
