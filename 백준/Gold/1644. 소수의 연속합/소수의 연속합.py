import sys
import math
input = sys.stdin.readline

n = int(input())
if n==1:
    print(0)
    exit(0)

arr = [True]*(n+1)
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        for j in range(i * i, n + 1, i):
            arr[j] = False
prime_list = []
for i in range(2,n+1):
    if arr[i] == True:
        prime_list.append(i)

left ,right = 0,0
temp_sum = prime_list[0]
cnt = 0

while right < len(prime_list):
    if temp_sum >n:
        temp_sum -= prime_list[left]
        left+=1
    else:
        if temp_sum==n:
            cnt+=1
        right+=1
        if right == len(prime_list):
            break
        temp_sum += prime_list[right]
print(cnt)
