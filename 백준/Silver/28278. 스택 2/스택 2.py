import sys
input = sys.stdin.readline
n = int(input())
st = []
for _ in range(n):
    word = input().split()
    if word[0] == '1' and len(word) > 1:
        st.append(int(word[1]))
    elif word[0]=='2':
        if st:
            print(st.pop(-1))
        else:
            print(-1)
    elif word[0]=='3':
        print(len(st))
    elif word[0]=='4':
        print(1 if not st else 0)
    elif word[0]=='5':
        if st:
            print(st[-1])
            continue
        else:
            print(-1)