def solution(s):
    s = s.upper()  # 대문자로 변환
    p_count = s.count('P')  # 'P' 개수
    y_count = s.count('Y')  # 'Y' 개수
    return p_count == y_count