import sys
from collections import deque
input = sys.stdin.readline
def valid_move(from_pos, to_pos):
    dx = abs(from_pos[0]-to_pos[0])
    dy = abs(from_pos[1]-to_pos[1])
    return dx**2 + dy**2 == 5
def conver_pos(position):
    col = ord(position[0])-ord('A')
    row = int(position[1])-1
    return (col, row)
moves = [input().strip() for _ in range(36)]
position = [conver_pos(move) for move in moves]
if len(set(position))!=36:
    print('Invalid')
    sys.exit(0)

for i in range(35):
    if not valid_move(position[i],position[i+1]):
        print('Invalid')
        sys.exit(0)
if not valid_move(position[-1],position[0]):
    print('Invalid')
    sys.exit(0)
print('Valid')