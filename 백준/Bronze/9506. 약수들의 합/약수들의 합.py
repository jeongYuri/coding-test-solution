import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n==-1:
        break

    res = []
    ran = n//2
    for i in range(1,ran+1):
        if n%i==0:
            res.append(i)

    if sum(res)==n:
        print(f"{n} = {' + '.join(map(str,res))}")
    else:
        print(f"{n} is NOT perfect.")