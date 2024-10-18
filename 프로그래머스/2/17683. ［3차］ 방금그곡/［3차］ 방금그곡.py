def change(music):
    return (music.replace('A#', 'a')
                 .replace('C#', 'c')
                 .replace('D#', 'd')
                 .replace('F#', 'f')
                 .replace('B#', 'b')
                 .replace('G#', 'g'))

def solution(m, musicinfos):
    answer = []
    m = change(m)  
    for idx, info in enumerate(musicinfos):
        start, end, title, melody = info.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        time = (end_h * 60 + end_m) - (start_h * 60 + start_m)

        changed = change(melody)
        if len(changed) == 0:
            continue

        melody = (changed * (time // len(changed))) + changed[:time % len(changed)]

        if m in melody:
            answer.append((time, idx, title))

    if not answer:
        return "(None)"
    elif len(answer)==1:
        return answer[0][2]
    else:
        answer.sort(key=lambda x: (-x[0], x[1]))
    
        return answer[0][2]