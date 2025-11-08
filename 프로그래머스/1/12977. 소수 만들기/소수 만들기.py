from itertools import combinations
def check(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    nums.sort()
    numbers = list(combinations(nums, 3))
    for num in numbers:
        temp = sum(num)
        if check(temp):
            answer+=1
    return answer