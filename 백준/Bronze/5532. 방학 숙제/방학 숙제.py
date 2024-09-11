import sys
input = sys.stdin.readline
import math
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
korean = math.ceil(a / c)
end_math = math.ceil(b / d)
max_day = max(korean,end_math)
play = l-max_day
print(play)