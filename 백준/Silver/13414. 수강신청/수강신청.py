import sys
input = sys.stdin.readline
from collections import OrderedDict

k, l = map(int, input().split())
students = [input().strip() for _ in range(l)]

sucess = OrderedDict()

for student in students:
    if student in sucess:
        del sucess[student]
    sucess[student] = True

count = 0
for student in sucess:
    print(student)
    count += 1
    if count == k:
        break