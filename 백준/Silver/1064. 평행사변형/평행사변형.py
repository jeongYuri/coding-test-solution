import sys
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def is_collinear(xa, ya, xb, yb, xc, yc):
    return (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa) == 0

def solution(xa, ya, xb, yb, xc, yc):
    p1 = 2 * (distance(xa, ya, xb, yb) + distance(xa, ya, xc, yc))
    p2 = 2 * (distance(xa, ya, xb, yb) + distance(xb, yb, xc, yc))
    p3 = 2 * (distance(xa, ya, xc, yc) + distance(xb, yb, xc, yc))
    return max(p1, p2, p3) - min(p1, p2, p3)

xa, ya, xb, yb, xc, yc = map(int, sys.stdin.readline().split())

if is_collinear(xa, ya, xb, yb, xc, yc):
    print(-1)
else:
    print(solution(xa, ya, xb, yb, xc, yc))
