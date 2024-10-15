def solution(nums):
    answer = 0
    poketmon = set(nums) #중복 제거해서 간략하게 하기 위해
    answer = min(len(poketmon),len(nums)//2)
    return answer