from collections import Counter

b = int(input())
arr = list(map(int, input().split()))

freq = Counter(arr)  

ngf = [-1] * b  

stack = []
for i in range(b-1, -1, -1):  
  
    while stack and freq[arr[stack[-1]]] <= freq[arr[i]]:
        stack.pop()
 
    if stack:
        ngf[i] = arr[stack[-1]]
    stack.append(i)

print(*ngf)
