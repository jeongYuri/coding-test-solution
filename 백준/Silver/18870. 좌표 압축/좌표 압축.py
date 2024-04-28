import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().rstrip().split()))
lists = sorted(list(set(nums)))
dictlist = dict(zip(lists,list(range(len(lists)))))
for x in nums:
    print(dictlist[x],end=' ')
