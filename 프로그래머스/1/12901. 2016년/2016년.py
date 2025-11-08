def solution(a, b):
    answer = ''
    month_d = [31,29,31,30,31,30,31,31,30,31,30,31]
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    total_day = sum(month_d[:a-1])+(b-1)

    return week[(total_day+5)%7]