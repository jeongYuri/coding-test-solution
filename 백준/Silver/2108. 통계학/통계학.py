import sys
input = sys.stdin.readline

t = int(input())
arr = []
for _ in range(t):
    n = int(input())
    arr.append(n)
arr.sort()
print(round(sum(arr)/t))
print(arr[(t//2)])
dic = dict()
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
mx = max(dic.values())
mx_dic = []
for i in dic:
    if mx==dic[i]:
        mx_dic.append(i)
if len(mx_dic)>1:
    print(mx_dic[1])
else:
    print(mx_dic[0])
print(max(arr)-min(arr))
