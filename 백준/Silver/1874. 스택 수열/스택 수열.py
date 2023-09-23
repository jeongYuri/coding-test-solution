import sys
input = sys.stdin.readline
N = int(input())
A = N*[0]

for i in range(N):
    A[i] = int(input())
answer = ""
stack = []
num = 1
result = True

for i in range(N):
  su = A[i]
  if su>= num:
    while su>=num:
        stack.append(num)
        num +=1
        answer +="+\n"
    stack.pop()
    answer +="-\n"
  else:
        n = stack.pop()
        if su<n:
            print("NO")
            result = False
            break
        else:
            answer +="-\n"
if result:
    print(answer)