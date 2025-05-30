t = int(input())
for _ in range(t):
    n, m = input().split()
    zero_to_one = 0
    one_to_zero = 0
    for a, b in zip(n, m):
        if a != b:
            if a == '0':
                zero_to_one += 1
            else:
                one_to_zero += 1
    print(max(zero_to_one, one_to_zero))
