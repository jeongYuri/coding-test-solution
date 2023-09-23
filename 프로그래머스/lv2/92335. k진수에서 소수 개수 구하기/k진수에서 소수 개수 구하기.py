def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    rebase = ''
    while n>0:
        n,mod = divmod(n,k)
        rebase+=str(mod)
    rebase = rebase[::-1].split('0')
    for i in rebase:
         if i != '':
            re = int(i, 10)
            if prime(re):
                answer += 1
    return answer
   
  