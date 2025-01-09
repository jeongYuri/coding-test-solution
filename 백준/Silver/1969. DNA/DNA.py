import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [input().strip() for _ in range(n)]
cnt, hab = 0,0
res = ''
for i in range(m):
    a,c,g,t = 0,0,0,0
    for j in range(n):
        if arr[j][i]=='T':
            t+=1
        elif arr[j][i]=='A':
            a+=1
        elif arr[j][i]=='C':
            c+=1
        elif arr[j][i]=='G':
            g+=1
    if max(a,c,g,t)==a:
        res+='A'
        hab += c+g+t
    elif max(a,c,g,t)==c:
        res+='C'
        hab+= a+g+t
    elif max(a,c,g,t)==g:
        res+='G'
        hab+= a+c+t
    elif max(a,c,g,t)==t:
        res +='T'
        hab+=a+c+g
print(res)
print(hab)