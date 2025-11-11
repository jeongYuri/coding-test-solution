def solution(msg):
    ans = []
    next_idx = 27
    dicti = {}
    for i in range(1, 27):
        dicti[chr(i + 64)] = i

    i = 0
    while i < len(msg):
        w = msg[i]
        while i + len(w) < len(msg) and msg[i:i + len(w) + 1] in dicti:
            w = msg[i:i + len(w) + 1]

        ans.append(dicti[w])

        if i + len(w) < len(msg):
            dicti[w + msg[i + len(w)]] = next_idx 
            next_idx += 1

        i += len(w)

    return ans
