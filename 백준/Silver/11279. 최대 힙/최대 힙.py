import sys
import heapq
input = sys.stdin.readline
mheap = []
n = int(input())
for i in range(n):
	num = int(input()) * -1
	if num == 0:
		print(heapq.heappop(mheap) * -1 if mheap else 0)
	else:
		heapq.heappush(mheap, num)