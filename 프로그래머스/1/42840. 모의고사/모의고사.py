def solution(answers):
    win = []
    st1 = [1,2,3,4,5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0,0,0]
    for i in range(len(answers)):
        if answers[i]==st1[(i%5)]:
            count[0]+=1
        if answers[i]==st2[(i%8)]:
            count[1]+=1
        if answers[i]==st3[(i%10)]:
            count[2]+=1
    for i in range(3):
        if count[i]==max(count):
            win.append(i+1)
    return win