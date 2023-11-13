t = int(input())

def DFS(count):
    global answer
    if count ==0:
        answer = max(int("".join(nums)),answer)
        return answer
    for i in range(legth):
        for j in range(i+1,legth):
            nums[i], nums[j] = nums[j], nums[i]
            temp_key = "".join(nums)
            if visited.get((temp_key,count-1),1):
                visited[(temp_key,count-1)]=0
                DFS(count-1)
            nums[i], nums[j] = nums[j], nums[i]

for tc in range(1,t+1):
    answer = -1
    nums, change = (input().split())
    nums = list(nums)
    legth = len(nums)
    change = int(change)
    visited = {}
    DFS(change)
    print(f'#{tc} {answer}')