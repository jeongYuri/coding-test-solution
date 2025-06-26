import sys
input = sys.stdin.readline


su = []
for i in range(5):
    su.append(int(input()))
su.sort()
print(int(sum(su)/5))
print(su[2])

