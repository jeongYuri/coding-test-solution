def solution(number, limit, power):
    ans = [1]
    for n in range(2,number+1):
        count =0
        for j in range(1,int(n**(1/2)+1)):
            if n % j ==0:
                count +=1
                if j**2 != n: #제곱이 되는 약수 중복 방지
                    count+=1
        if count>limit:
            count = power
            ans.append(count)
        else:
            ans.append(count)
            
    return sum(ans)