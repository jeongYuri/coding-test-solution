import sys; h, m = map(int, sys.stdin.readline().split()); print((h-1 if m<45 else h) if h != 0 or m >= 45 else 23, m+15 if m<45 else m-45)
