def solution(numbers, hand):
    answer = ""
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    left_pos = keypad['*']
    right_pos = keypad['#']
    
    for num in numbers:
        if num in [1,4,7]:#왼쪽으로..
            answer +='L'
            left_pos = keypad[num]
        elif num in [3,6,9]:
            answer +='R'
            right_pos = keypad[num]
        else:
            lx = abs(left_pos[0]-keypad[num][0])+abs(left_pos[1]-keypad[num][1])
            rx = abs(right_pos[0]-keypad[num][0])+abs(right_pos[1]-keypad[num][1])
            if lx<rx:
                answer+='L'
                left_pos = keypad[num]
            elif lx>rx:
                answer +='R'
                right_pos = keypad[num]
            else:
                if hand == 'right':
                    answer+='R'
                    right_pos = keypad[num]
                else:
                    answer+='L'
                    left_pos = keypad[num]
                
    return answer