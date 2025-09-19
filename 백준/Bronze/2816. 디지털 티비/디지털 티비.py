import sys
input = sys.stdin.readline

n = int(input())
channel = [input().strip() for _ in range(n)]
pos1 = channel.index("KBS1")
pos2 = channel.index("KBS2")

if pos1>pos2:
    pos2+=1
print('1'*pos1+'4'*pos1 + '1'*pos2 +'4'*(pos2-1))
