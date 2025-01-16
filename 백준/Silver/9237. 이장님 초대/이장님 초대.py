import sys
input = sys.stdin.readline


n = int(input())
tree = list(map(int,input().split()))
tree.sort(reverse = True)
day = 0
for i in range(n):
    day = max(day, tree[i]+i+1)
print(day+1)