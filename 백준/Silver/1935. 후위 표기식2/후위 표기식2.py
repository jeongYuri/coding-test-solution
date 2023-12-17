n = int(input())
sen = input()
alph= [0]*n
for i in range(n):
    alph[i] = int(input())
stack = []

for i in sen:
    if 'A'<=i<='Z':
        stack.append(alph[ord(i)-ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        if i=='+':
            stack.append(str1+str2)
        elif i=='-':
            stack.append(str1-str2)
        elif i=='*':
            stack.append(str1*str2)
        elif i=='/':
            stack.append(str1/str2)

print('%.2f' %stack[0])