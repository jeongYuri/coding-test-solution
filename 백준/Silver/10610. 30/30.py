import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
if 0 in n and sum(n) % 3 == 0:  
    n.sort(reverse=True)  
    print(''.join(map(str, n))) 
else:
    print(-1)