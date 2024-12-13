import sys
input = sys.stdin.readline
n,m = map(int,input().split())
package = []
single = []
for _ in range(m):
    p,s = map(int,input().split())
    package.append(p)
    single.append(s)
cost = 0
min_package = min(package)
min_single = min(single)

cost = min((n // 6) * min_package + (n % 6) * min_single,  
           ((n // 6) + 1) * min_package,
           n * min_single)

print(cost)