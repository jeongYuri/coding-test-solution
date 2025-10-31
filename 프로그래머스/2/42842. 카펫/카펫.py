def solution(brown, yellow):
    total = brown+yellow
    for i in range(3,total+1):
        w = total//i
        if total %i==0:
            if (w-2)*(i-2)==yellow:
                return [w,i]
  