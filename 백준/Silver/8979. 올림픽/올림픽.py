import sys
input = sys.stdin.readline

n,k = map(int,input().split())
countries = []
for _ in range(n):
    country = list(map(int, input().split()))
    countries.append((country[1], country[2], country[3], country[0]))  #순위정하기 금메달->은메달->동메달
countries.sort(reverse = True, key = lambda x:(x[0],x[1],x[2]))
ranks = [0]*(n+1)
rank = 1 #현재 등수

for i in range(n):
    if i>0 and countries[i][:3] == countries[i-1][:3]: #이전에 메달이 같은 경우
        ranks[countries[i][3]] = ranks[countries[i-1][3]]
    else:
        ranks[countries[i][3]] = rank
    rank +=1
print(ranks[k])

