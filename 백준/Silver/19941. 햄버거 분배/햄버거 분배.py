import sys
input = sys.stdin.readline

n, k = map(int, input().split())
hambuger = list(input().strip())
cnt = 0

for i in range(n):
    if hambuger[i] == 'P':
        for j in range(max(0, i - k), min(n, i + k + 1)):
            if hambuger[j] == 'H': 
                cnt += 1
                hambuger[j] = '0'
                break

print(cnt)