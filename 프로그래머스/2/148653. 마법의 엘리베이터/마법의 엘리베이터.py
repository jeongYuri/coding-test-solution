def solution(storey):
    ans = 0
    while storey > 0:
        digit = storey % 10
        next_digit = (storey // 10) % 10
        
        if digit > 5:
            ans += 10 - digit
            storey = storey // 10 + 1
        elif digit < 5:
            ans += digit
            storey //= 10
        else: 
            if next_digit >= 5:
                ans += 5
                storey = storey // 10 + 1
            else:
                ans += 5
                storey //= 10
                
    return ans