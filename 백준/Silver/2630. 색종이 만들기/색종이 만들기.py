import sys
input = sys.stdin.readline
def cnt_color(x,y,n):
    global w, b
    initial_color = paper[x][y]
    same_color = True

    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != initial_color:
                same_color = False
                break
        if not same_color:
            break
    if same_color :
        if initial_color ==0:
            w +=1
        else:
            b+=1
    else:
        half = n//2
        cnt_color(x,y, half)
        cnt_color(x,y+half,half)
        cnt_color(x+half, y, half)
        cnt_color(x+half,y+half, half)
n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]

w,b = 0,0
cnt_color(0,0,n)
print(w)
print(b)