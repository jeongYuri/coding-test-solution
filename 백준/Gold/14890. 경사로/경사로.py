import sys
input = sys.stdin.readline
def check_line(line,l,n):
    slope = [False]*n
    for i in range(1,n):
        if abs(line[i]-line[i-1])>1:#높이 차가 2이상이면 불가능
            return False
        if(line[i]>line[i-1]): #오르막길
            for j in range(1,l+1):
                if i - j < 0 or line[i - 1] != line[i - j] or slope[i - j]:
                    return False
                slope[i-j] = True
        elif line[i]<line[i-1]: #내리막길
            for j in range(l):
                if i+j>=n or line[i]!=line[i+j] or slope[i+j]:
                    return False
                slope[i+j] = True
    return True
def cnt_path(graph, l,n):
    cnt = 0
    for row in graph:
        if check_line(row,l,n):
            cnt +=1
    for col in zip(*graph):
        if check_line(col,l,n):
            cnt +=1
    return cnt


n, l = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
print(cnt_path(graph,l,n))