import sys
import heapq

input = sys.stdin.readline

n = int(input())
nums = [int(input().rstrip())for _ in range(n)]
heapq.heapify(nums)  
sorted_nums = [heapq.heappop(nums) for _ in range(n)]
sys.stdout.write("\n".join(map(str, sorted_nums)) + "\n")