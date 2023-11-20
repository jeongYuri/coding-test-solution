subway = []
cnt  = 0
for k in range(1,11):
    o,i = map(int,input().split())
    cnt-=o
    cnt+=i
    subway.append(cnt)

print(max(subway))