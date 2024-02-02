import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
arr = []
while True:
    try:
        arr.append(int(input().rstrip()))
    except:
        break
def postorder(root_idx,end_idx):
    if root_idx>end_idx:
        return
    global arr
    right_start = end_idx+1
    for i in range(root_idx+1,end_idx+1):
        if arr[root_idx]<arr[i]:
            right_start=i
            break
    postorder(root_idx+1,right_start-1)
    postorder(right_start,end_idx)
    print(arr[root_idx])
postorder(0,len(arr)-1)