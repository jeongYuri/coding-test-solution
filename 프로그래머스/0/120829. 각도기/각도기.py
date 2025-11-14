def solution(angle):
    return 3 if 90 < angle < 180 else \
           2 if angle == 90 else \
           1 if 0 < angle < 90 else 4