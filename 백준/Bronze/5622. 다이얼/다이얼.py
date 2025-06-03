import sys
input = sys.stdin.readline

word = input().strip()
dial = ["ABC",    # 2
    "DEF",    # 3
    "GHI",    # 4
    "JKL",    # 5
    "MNO",    # 6
    "PQRS",   # 7
    "TUV",    # 8
    "WXYZ"    # 9
 ]

time = 0
for ch in word:
    for i in range(len(dial)):
        if ch in dial[i]:
            time += i+3
            break
print(time)