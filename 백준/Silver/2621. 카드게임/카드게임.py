import sys
input = sys.stdin.readline
from collections import Counter
colors = []
numbers = []
for _ in range(5):
    card,num = input().split()
    colors.append(card)
    numbers.append(int(num))
numbers.sort()
cnt = Counter(numbers)

same_color = len(set(colors))==1 #모든 색이 같으면 True
is_seq = all(numbers[i]+1== numbers[i+1] for i in range(4)) #연속된 숫자면 True
max_num = max(numbers)
score = 0

if same_color and is_seq:
    score = max_num+900
elif 4 in cnt.values():
    num = [k for k ,v in cnt.items() if v==4][0]
    score = num+800
elif sorted(cnt.values())==[2,3]:
    three = [k for k, v in cnt.items() if v==3][0]
    two = [k for k, v in cnt.items() if v==2][0]
    score = three *10 + two + 700
elif same_color:
    score = max_num +600
elif is_seq:
    score = max_num + 500
elif 3 in cnt.values():
    num = [k for k, v in cnt.items() if v==3][0]
    score = num + 400
elif list(cnt.values()).count(2)==2:
    pairs = sorted([k for k, v in cnt.items() if v==2],reverse=True)
    score = pairs[0]*10+pairs[1]+300
elif 2 in cnt.values():
    num = [k for k, v in cnt.items() if v==2][0]
    score =  num +200
else:
    score = max_num +100
print(score)