str = input()
st = list(str)
answer = []
for i in st:
    if i.isupper()==True:
        answer.append(i.lower())
    else:
        answer.append(i.upper())
print(''.join(answer))