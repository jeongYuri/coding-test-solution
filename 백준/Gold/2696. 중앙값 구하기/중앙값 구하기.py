import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())
    nums = []
    while len(nums) < m:
        nums.extend(map(int, input().split()))

    res = []
    for i in range(m):
        if i % 2 == 0: 
            temp = sorted(nums[:i + 1])
            res.append(temp[i // 2])

    print(len(res))
    for i in range(0, len(res), 10):
        print(*res[i:i + 10])
