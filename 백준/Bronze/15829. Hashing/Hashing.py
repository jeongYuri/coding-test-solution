n = int(input())
data = list(input())
res = 0

for i in range(n):
    res+=((ord(data[i])-96)*(31**i))
print(res %1234567891)