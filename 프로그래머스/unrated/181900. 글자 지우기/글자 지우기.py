def solution(my_string, indices):
    answer = ''
    mys = list(my_string)
    for i in sorted(indices, reverse=True):
        del mys[i]
    return ''.join(mys)