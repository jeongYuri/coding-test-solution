def solution(s, skip, index):
    answer = ''
    alph = [chr(i) for i in range(ord('a'),ord('z')+1)]
    for sk in skip:
        if sk in alph:
            alph.remove(sk)
    for ch in s:
        pos = alph.index(ch)
        new_pos = (pos+index)%len(alph)
        answer+= alph[new_pos]
    return answer