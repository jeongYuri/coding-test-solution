import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())

titles = []     
thresholds = [] 

for _ in range(N):
    line = input().split()
    title = line[0]         
    threshold = int(line[1]) 
    titles.append(title)
    thresholds.append(threshold)

for _ in range(M):
    power = int(input())
    idx = bisect.bisect_left(thresholds, power)
    print(titles[idx])
