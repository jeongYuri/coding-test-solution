def solution(wallet, bill):
    answer = 0
    w, h = wallet
    bw, bh = bill
    while True:
        if (bw<=w and bh<=h) or (bw<=h and bh<=w):
            break
        if bw>=bh:
            bw//=2
        else:
            bh//=2
        answer+=1
    return answer