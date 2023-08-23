def solution(str_list):
    answer = []
    for s in str_list:       
        if s =="l":
            text = "s"
            if len(text)==1:
                a = str_list.index('l')
                return str_list[:a]
        elif s =="r":
            text = "r"
            if len(text)==1:
                a = str_list.index('r')
                return str_list[a+1:]
    return answer