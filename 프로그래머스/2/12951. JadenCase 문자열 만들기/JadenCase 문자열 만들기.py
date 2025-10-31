def solution(s):
    ans = []
    arrs = arrs = s.split(" ")
    for ch in arrs:
        if ch:
            ans.append(ch[0].upper()+ch[1:].lower())
        else:
            ans.append('')
    return ' '.join(ans)