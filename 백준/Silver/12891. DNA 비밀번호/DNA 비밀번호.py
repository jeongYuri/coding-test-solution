import sys
input = sys.stdin.readline
checkList = [0]*4
myList = [0]*4
check = 0
def myadd(a):
  global chekList, myList, check
  if a=='A':
    myList[0]+=1
    if myList[0] == checkList[0]:
      check +=1
  elif a=='C':
    myList[1]+=1
    if myList[1] == checkList[1]:
      check+=1
  elif a=='G':
     myList[2]+=1
     if myList[2] == checkList[2]:
       check +=1
  elif a=='T':
     myList[3]+=1
     if myList[3] == checkList[3]:
       check +=1
def myremove(a):
  global checkList, myList, check
  if a=='A':
    if myList[0]==checkList[0]:
      check -=1
    myList[0] -=1
  elif a=='C':
    if myList[1] ==checkList[1]:
      check -=1
    myList[1] -=1
  elif a=='G':
    if myList[2]==checkList[2]:
      check -=1
    myList[2] -=1
  elif a=='T':
    if myList[3]==checkList[3]:
      check -=1
    myList[3] -=1
      
S,P = map(int,input().split())
A = list(input())
answer = 0
checkList = list(map(int,input().split()))

for i in range(4):
  if checkList[i]==0:
    check +=1
for i in range(P):
  myadd(A[i])
if check==4:
  answer +=1
for i in range(P,S):
  j = i-P
  myadd(A[i])
  myremove(A[j])
  if check  ==4:
    answer +=1
print(answer)