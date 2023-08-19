def solution(date1, date2):
    for x, y in zip(date1, date2):
        if date1<date2:
            return 1
        else:
            return 0
    
