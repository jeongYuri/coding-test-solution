import sys
import math
input = sys.stdin.readline

s = str(input()).rstrip()
t = str(input()).rstrip()
lcm_length = math.lcm(len(s),len(t))
if (s * (lcm_length // len(s))) == (t * (lcm_length // len(t))):
    print(1)
else:
    print(0)