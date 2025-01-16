import sys
input = sys.stdin.readline

target ='UCPC'
world = input().strip()
idx = 0

for char in world:
    if char==target[idx]:
        idx+=1
        if idx == len(target):
            print("I love UCPC")
            break
else:
    print("I hate UCPC")