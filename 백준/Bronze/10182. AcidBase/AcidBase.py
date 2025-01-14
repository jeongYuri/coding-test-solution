import math


n = int(input())

for _ in range(n):
    data = input().split(' = ')
    if data[0] == "H":
        H_plus = float(data[1])
        pH = -math.log10(H_plus)
    elif data[0] == "OH":
        OH_minus = float(data[1])
        pOH = -math.log10(OH_minus)
        pH = 14 - pOH
    print(f"{pH:.2f}")
