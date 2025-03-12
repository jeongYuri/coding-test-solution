import sys
input = sys.stdin.readline

n = int(input())
scores = list(input().split()for _ in range(n))
score1, score2 = 0,0
win_time1 , win_time2 = 0,0
prev_time = 0

def time_to(time_str):
    minutes, seconds = map(int,time_str.split(":"))
    return minutes*60+seconds
def second_to(seconds):
    return f"{seconds // 60:02}:{seconds % 60:02}"
for score in scores:
    num = int(score[0])
    current_time = time_to(score[1])

    if score1>score2:
        win_time1 += current_time - prev_time
    elif score2>score1:
        win_time2 += current_time - prev_time
    if num ==1:
        score1+=1
    else:
        score2+=1
    prev_time = current_time
if score1>score2:
    win_time1 += 48*60-prev_time
elif score2>score1:
    win_time2 += 48*60 -prev_time

print(second_to(win_time1))
print(second_to(win_time2))
