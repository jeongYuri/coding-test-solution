import sys
A= sys.stdin.readline
N = int(A())
for i in range(N):
  S,P= map(int,A().split())
  print(S+P)