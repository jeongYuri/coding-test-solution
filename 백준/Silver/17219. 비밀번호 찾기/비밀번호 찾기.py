import sys
input = sys.stdin.readline

n, m = map(int, input().split())
site_to_pw = {}
for _ in range(n):
    site, pw = input().split()
    site_to_pw[site] = pw
for _ in range(m):
    want = input().strip()
    print(site_to_pw.get(want, '')) 