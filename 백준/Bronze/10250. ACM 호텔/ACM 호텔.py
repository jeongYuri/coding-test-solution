import sys
input = sys.stdin.readline
def customer(h,w,n):
    floor = (n-1)%h+1
    room = (n-1)//h+1
    ans  = floor * 100 + room
    return ans
tc = int(input())
for _ in range(tc):
    h,w,n = map(int,input().split())
    res = customer(h,w,n)
    print(res)
