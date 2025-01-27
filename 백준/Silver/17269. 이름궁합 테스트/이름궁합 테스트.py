import sys
input = sys.stdin.readline
alpha = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3, 'I': 1, 'J': 1,
    'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2,
    'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1
}
n,m = map(int,input().split())
a,b = map(str,input().split())

names = []

for i in range(min(n,m)):
    names.append(alpha[a[i]])
    names.append(alpha[b[i]])
if n > m:
    names.extend(alpha[ch] for ch in a[m:])
elif m > n:
    names.extend(alpha[ch] for ch in b[n:])

while len(names)>2:
    scores = []
    for i in range(len(names)-1):
        value = (names[i]+names[i+1])%10
        scores.append(value)
    names = scores
res = names[0]*10 + names[1]
if names[0] == 0:
    print(str(names[1]) + "%")
else:
    print(str(res) + "%")

