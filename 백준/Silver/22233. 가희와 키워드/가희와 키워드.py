import sys
input = sys.stdin.readline

n,m = map(int,input().split())
memo = set(input().strip() for _ in range(n))

for idx in range(1, m + 1):
    words = input().strip().split(',')
    memo -= set(words)
    print(len(memo))



