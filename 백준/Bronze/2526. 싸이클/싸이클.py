n, p = map(int, input().split())
l = []
a = n

while True:
    a = (a * n) % p
    if a in l:
        print(len(l) - l.index(a))
        break
    l.append(a)
