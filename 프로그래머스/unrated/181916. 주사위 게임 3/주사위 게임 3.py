def solution(a, b, c, d):
    nums = [a,b,c,d]
    counts = [nums.count(i) for i in nums]
    if max(counts)==4:
        return 1111*a
    elif max(counts)==3:
        p=nums[counts.index(3)]
        q=nums[counts.index(1)]
        return (10*p+q)**2
    elif max(counts)==2:
        if min(counts) == 2:
            if a==b:
                return (a + c) * abs(a - c) 
            else: 
                return (a + b) * abs(a - b)
        else:
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(nums)
        
   