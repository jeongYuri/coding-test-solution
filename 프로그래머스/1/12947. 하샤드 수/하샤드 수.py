
def solution(x):
    num = [int(digit) for digit in str(x)]
    nums = sum(num)
    if x % nums == 0:
        return True
    return False