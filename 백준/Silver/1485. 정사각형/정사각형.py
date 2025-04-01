import sys
input = sys.stdin.readline

def is_squeare(points):
    points.sort()
    x1,y1 = points[0]
    x2,y2 = points[1]
    x3,y3 = points[2]
    x4,y4 = points[3]

    d1 = (x2-x1)**2 + (y2-y1)**2
    d2 = (x3-x1)**2 + (y3-y1)**2
    d3 = (x4-x2)**2 + (y4-y2)**2
    d4 = (x4-x3)**2 + (y4-y3)**2
    diag1 = (x4-x1)**2 + (y4-y1)**2
    diag2 = (x3-x2)**2 + (y3-y2)**2

    return d1==d2==d3==d4 and diag1==diag2

t = int(input())
ans = []
for _ in range(t):
    points = [tuple(map(int,input().split()))for _ in range(4)]
    ans.append(1 if is_squeare(points) else 0)
print("\n".join(map(str, ans)))