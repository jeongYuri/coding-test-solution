t = int(input())
for _ in range(t):
    n = int(input())
    closet = {}
    for i in range(n):
        name,category = map(str,input().split())
        if category not in closet:
            closet[category] =[name]
        else:
            closet[category].append(name)
    answer = 1
    for ck in closet.keys():
        answer *= (len(closet[ck])+1)
    print(answer-1)