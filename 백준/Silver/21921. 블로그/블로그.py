import sys
input = sys.stdin.readline

n,x = map(int,input().split())
visitors = list(map(int,input().split()))

current_sum = sum(visitors[:x])
max_sum = current_sum
cnt = 1

for i in range(x,n):
    current_sum = current_sum - visitors[i-x] + visitors[i]
    if current_sum>max_sum:
        max_sum = current_sum
        cnt =1
    elif current_sum == max_sum:
        cnt +=1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(cnt)
