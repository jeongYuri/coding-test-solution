import sys
input = sys.stdin.readline

def digit_sum(n):
    return sum(map(int, str(n)))
x_str = input().strip()
if len(x_str) == 1:
    print(0)
    print("YES" if int(x_str) % 3 == 0 else "NO")
else:
    cnt = 0
    num = int(x_str)
    while num >= 10:
        num = digit_sum(num)
        cnt += 1
    print(cnt)
    print("YES" if num % 3 == 0 else "NO")