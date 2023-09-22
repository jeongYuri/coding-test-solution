def solution(numbers, target):
    def cal(idx,hab):
        nonlocal count
        if idx == len(numbers):
            if hab == target:
                count +=1
            return count
        cal(idx+1,hab+numbers[idx])
        cal(idx+1,hab-numbers[idx])  
    count = 0
    cal(0,0)
    return count