import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * 101 for _ in range(101)]
for _ in range(n): #색종이 1로 채우기
    x,y = map(int,input().split())
    for row in range(x,x+10):
        for col in range(y,y+10):
            arr[row][col] = 1
res = 0
for i in arr:
    res += sum(i)
print(res)