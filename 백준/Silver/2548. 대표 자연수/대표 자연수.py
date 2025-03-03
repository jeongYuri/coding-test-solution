import sys
input = sys.stdin.readline



n  = int(input())
arr = list(map(int,input().split()))
arr.sort()

left, right = 0,sum(arr)-arr[0]*n
ans, ans_sum = 0,right

for i in range(1,n):
  height = arr[i]-arr[i-1]
  left += height * i
  right -= height*(n-i)

  if left+right < ans_sum:
    ans  = i
    ans_sum = left+right
print(arr[ans])



