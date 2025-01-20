import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int,input().split()))
print(*sorted(number))