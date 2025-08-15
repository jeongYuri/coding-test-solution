import sys
input = sys.stdin.readline

s = input().rstrip()
nums = int(input())
pre = [[0]*26]

for i, ch in enumerate(s):
    nxt = pre[i][:]
    nxt[ord(ch)-97] +=1
    pre.append(nxt)
for _ in range(nums):
    char, l,r = input().split()
    idx = ord(char)-97
    print(pre[int(r)+1][idx]-pre[int(l)][idx])



