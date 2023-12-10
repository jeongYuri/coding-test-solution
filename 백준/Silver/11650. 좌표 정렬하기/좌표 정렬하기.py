import sys
input = sys.stdin.readline

n = int(input())
board = []

for i in range(n):
    x, y = map(int, input().split())
    board.append((x,y))

board.sort(key=lambda nums: (nums[0], nums[1]))

for num in board:
    print(num[0], num[1])