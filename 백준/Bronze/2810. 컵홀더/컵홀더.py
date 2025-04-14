n = int(input())
seats = input()

couple = seats.count('LL')

cupholders = len(seats) + 1 - couple

print(min(n, cupholders))
