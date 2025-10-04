import sys
input = sys.stdin.readline

t = int(input())
words = [input().strip() for _ in range(t)]

weight = {} #가중치~
for word in words:
    length = len(word)
    for i, ch in enumerate(word):
        w = 10**(length-i-1)
        if ch in weight:
            weight[ch]+=w
        else:
            weight[ch]= w
sorted_letter = sorted(weight.items(), key = lambda x:x[1],reverse=True)
num = 9
to_num = {}
for ch, a in sorted_letter:
    to_num[ch] = num
    num-=1
res = 0
for word in words:
    num_value = 0
    for ch in word:
        num_value = num_value*10+to_num[ch]
    res+= num_value
print(res)
