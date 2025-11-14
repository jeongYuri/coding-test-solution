import math

def solution(numer1, denom1, numer2, denom2):

    lcm = denom1 * denom2 // math.gcd(denom1, denom2)
   
    n1 = numer1 * (lcm // denom1)
    n2 = numer2 * (lcm // denom2)
  
    top = n1 + n2
   
    g = math.gcd(top, lcm)
    
    return [top // g, lcm // g]
