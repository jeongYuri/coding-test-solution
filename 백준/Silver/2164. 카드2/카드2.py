from collections import deque
n=int(input())
md = deque()
for i in range(1,n+1):
    md.append(i)
while len(md)>1:
    md.popleft()
    md.append(md.popleft())

print(md[0])