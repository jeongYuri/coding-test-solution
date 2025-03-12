import sys
input = sys.stdin.readline

king, stone, n = input().split()
n = int(n)

kx, ky = ord(king[0]) - ord('A') + 1, int(king[1])  # A~H → 1~8 변환
sx, sy = ord(stone[0]) - ord('A') + 1, int(stone[1])
move_dict = {
    "R": (1, 0), "L": (-1, 0), "B": (0, -1), "T": (0, 1),
    "RT": (1, 1), "LT": (-1, 1), "RB": (1, -1), "LB": (-1, -1)
} #이동방향 정의
commands = [input().strip() for _ in range(n)]

for command in commands:
    if command in move_dict:
        dx, dy = move_dict[command]
        nkx,nky = kx+dx , ky+dy #킹의 새로운 위치

        if(nkx,nky) == (sx,sy):
            nsx, nsy = sx+dx, sy+dy
            if 1<= nsx<=8 and 1<=nsy<=8:
                kx,ky = nkx, nky
                sx,sy = nsx, nsy
        else:
            if 1<= nkx <= 8 and 1<= nky <=8:
                kx, ky = nkx, nky
print(chr(kx+ord('A')-1)+str(ky))
print(chr(sx+ord('A')-1)+str(sy))

