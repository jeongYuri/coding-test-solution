import sys
input = sys.stdin.readline
ham1 = int(input())
ham2 = int(input())
ham3 = int(input())
cola = int(input())
sidar = int(input())
ham = min(ham1, ham2, ham3)
drink = min(cola,sidar)
print((ham+drink)-50)