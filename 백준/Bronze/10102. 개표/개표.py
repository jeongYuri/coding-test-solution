import sys
input = sys.stdin.readline

t = int(input())
votes = input().strip()
a_count = votes.count('A')
b_count = votes.count('B')

if a_count > b_count:
    print('A')
elif a_count<b_count:
    print('B')
else:
    print('Tie')