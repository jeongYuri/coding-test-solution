import sys
input = sys.stdin.readline

n,m = map(int,input().split())
pi = list(int(input()) for _ in range(m))
pi.sort()

max_revenue = 0
best_price = 0
for i in range(m):
    price = pi[i]
    buyers = min(n,m-i)
    revenue = price*buyers

    if revenue>max_revenue:
        max_revenue = revenue
        best_price = price
print(best_price, max_revenue)

