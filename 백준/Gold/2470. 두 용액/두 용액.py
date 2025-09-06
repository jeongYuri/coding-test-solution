import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left, right = 0, n-1
min_sum = float('inf')
answer = (0,0)

while left<right:
    total = liquid[left]+liquid[right]

    if abs(total)<abs(min_sum):
        min_sum = total
        answer = (liquid[left],liquid[right])
    if total<0:
        left+=1
    elif total>0:
        right-=1
    else:
        break

print(answer[0],answer[1])

