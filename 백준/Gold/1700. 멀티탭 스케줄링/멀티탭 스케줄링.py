import sys
input = sys.stdin.readline


n,k = map(int,input().split())
order = list(map(int,input().split()))
plug = []
res = 0
for i in range(k):
    if order[i] in plug:
        continue
    if len(plug)<n:
        plug.append(order[i])
        continue
    farthset =-1
    delete = -1
    for j in range(len(plug)):
        try:
            next_use = order[i+1:].index(plug[j])#다음으로 사용할 위치
        except ValueError:
            next_use = float('inf') #앞으로 사용 ㄴㄴ
        if next_use>farthset:
            farthset = next_use
            delete = j
    plug[delete] = order[i]
    res+=1
print(res)