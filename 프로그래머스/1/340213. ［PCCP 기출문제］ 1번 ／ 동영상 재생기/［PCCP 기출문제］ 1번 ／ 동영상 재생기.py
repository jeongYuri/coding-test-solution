def to_seconds(time_str):
    mm,ss = map(int,time_str.split(":"))
    return mm*60+ss
def to_time(second):
    mm = second//60
    ss = second%60
    return f"{mm:02}:{ss:02}"

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)
    if op_start<= pos<=op_end:
            pos = op_end
    for cmd in commands:
        if cmd=='next':
            pos = min(video_len, pos+10)
        elif cmd=='prev':
            pos = max(0,pos-10)
        if op_start<= pos<=op_end:
            pos = op_end
    return to_time(pos)