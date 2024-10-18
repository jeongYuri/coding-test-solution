def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def nodiv(array, gcd_value):
    for n in array:
        if n % gcd_value == 0:
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0
    gcda = arrayA[0]
    for a in arrayA[1:]:
        gcda = gcd(a, gcda)
    gcdb = arrayB[0]
    for b in arrayB[1:]:
        gcdb = gcd(b, gcdb)
    if nodiv(arrayA, gcdb):
        answer = max(answer, gcdb)
    if nodiv(arrayB, gcda):
        answer = max(answer, gcda)
        
    return answer