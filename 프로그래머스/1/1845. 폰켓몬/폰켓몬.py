def solution(nums):
    unique = len(set(nums))
    select = len(nums)//2
    return min(unique, select)