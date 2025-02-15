import sys
input = sys.stdin.readline

word = input().strip()
bomb = input().strip()

st = []
for char in word:
    st.append(char)
    if len(st)>=len(bomb) and ''.join(st[-len(bomb):])==bomb:
        del st[-len(bomb):]
result = ''.join(st)
if result == "":
    print("FRULA")
else:
    print(result)