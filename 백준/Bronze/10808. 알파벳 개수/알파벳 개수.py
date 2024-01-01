from string import ascii_lowercase
alph = {}
for i in ascii_lowercase:
    alph[i]=0
word = list(input())
for i in word:
    if i in alph:
        alph[i]+=1
for k,v in alph.items():
    print(v,end=' ')