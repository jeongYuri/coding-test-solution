import sys, heapq
input = sys.stdin.readline
n = int(input())  
q = []
for i in range(n):
    num_list = list(map(int, input().split()))
    for num in num_list:
        if len(q) < n:
            heapq.heappush(q, num)
        elif q[0] < num:
            heapq.heappush(q, num)
            heapq.heappop(q)  
print(q[0])