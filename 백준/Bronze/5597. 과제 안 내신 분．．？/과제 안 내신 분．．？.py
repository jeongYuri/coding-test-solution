import sys
input = sys.stdin.readline

stduent = [i for i in range(1,31)]
for _ in range(28):
    ss = int(input())
    if ss in stduent:
        stduent.remove(ss)
for s in sorted(stduent):
    print(s)
