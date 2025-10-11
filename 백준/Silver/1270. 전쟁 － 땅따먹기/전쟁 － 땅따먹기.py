import sys
input = sys.stdin.readline

n = int(input())
boards = [list(map(int,input().split()))for _ in range(n)]
for board in boards:
    nums = board[0]
    sol = board[1:]
    cnt = {}
    for i in sol:
        if i not in cnt:
            cnt[i]  = 1
        else:
            cnt[i]+=1
    res = 0
    ma = nums/2
    for k,v in cnt.items():
        if v> ma:
            res = k
            break
    if res == 0:
        print("SYJKGW")
    else:
        print(res)