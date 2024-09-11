import sys
input = sys.stdin.readline

minguk = list(map(int,input().split()))
mansu = list(map(int,input().split()))
min_score = sum(minguk)
man_score = sum(mansu)
print(min_score if min_score == man_score else max(min_score, man_score))

