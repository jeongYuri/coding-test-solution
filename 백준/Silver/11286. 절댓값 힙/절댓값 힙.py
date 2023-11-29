from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
n = int(input())
md = PriorityQueue()

for i in range(n):
    request = int(input())
    if request ==0:
        if md.empty():
            print('0\n')
        else:
            temp = md.get()
            print(str((temp[1]))+'\n')
    else:
        md.put((abs(request),request))