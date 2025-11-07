

def solution(s, n):
    answer = ''
    for ch in s:
        if ch.islower():
            answer += chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
        elif ch.isupper(): 
            answer += chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        else: 
            answer += ch
    return answer