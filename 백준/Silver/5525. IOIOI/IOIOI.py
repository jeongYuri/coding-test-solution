import sys
input = sys.stdin.readline

def find(s,text):
    count,start = 0,0

    while True:
        start = s.find(text,start)
        if start == -1:
            break
        count +=1
        start +=1
    return count

n = int(input())
m = int(input())
s = input()
text = 'I'+'OI'*(n-1)+'OI'
ans = find(s,text)
print(ans)
