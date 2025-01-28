import sys
input = sys.stdin.readline

text = str(input()).rstrip()
reverse = text[::-1]
if text==reverse:
    print(1)
else:
    print(0)
