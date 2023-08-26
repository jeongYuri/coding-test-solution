def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}
    left = [1,4,7]
    right = [3,6,9]
    lehand = '*'
    rihand = '#'
    
    for i in numbers:
        if i in left:
            answer +='L'
            lehand = i
        elif i in right:
            answer +='R'
            rihand = i
        else:
            curpos = key_dict[i]
            lpos=key_dict[lehand]
            rpos=key_dict [rihand]
            ldist=abs(curpos[0]-lpos[0])+abs(curpos[1]-lpos[1])
            rdist=abs(curpos[0]-rpos[0])+abs(curpos[1]-rpos[1])
            
            if ldist<rdist:
                answer +='L'
                lehand = i
            elif ldist>rdist:
                answer +='R'
                rihand = i
            else:
                if hand=='left':
                    answer +='L'
                    lehand = i
                else:
                    answer +='R'
                    rihand = i
            
    return answer