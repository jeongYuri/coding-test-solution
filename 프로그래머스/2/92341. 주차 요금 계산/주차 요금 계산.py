from datetime import datetime
import math

def solution(fees, records):
    answer = {record.split()[1]:0 for record in records}
    car = {}
    for record in records:
        time, number, state = record.split()
        if state == 'IN':
            car[number] = datetime.strptime(time, "%H:%M")
        else: #out
            pay = str(datetime.strptime(time,"%H:%M")-car[number])
            pay = int(pay.split(":")[0])*60 + int(pay.split(":")[1])
            answer[number]+= pay
            del car[number] #출차했다는것
    if len(car)>0:
        for c in car:
            pay = str(datetime.strptime('23:59',"%H:%M")-car[c])
            pay = int(pay.split(":")[0])*60 + int(pay.split(":")[1])
            answer[c] +=pay
    answer = sorted(answer.items())
    for i in range(len(answer)):
        if answer[i][1]<=fees[0]:
            answer[i] = fees[1]
        else: 
            answer[i] = fees[1] + math.ceil((answer[i][1] - fees[0])/fees[2]) * fees[3]
    return answer   
    