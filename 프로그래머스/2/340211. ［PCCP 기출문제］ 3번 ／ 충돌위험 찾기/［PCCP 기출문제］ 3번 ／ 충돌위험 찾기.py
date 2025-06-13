from collections import defaultdict

def solution(points, routes):
    time_map = defaultdict(int)
    for route in routes:
        t = 0
        cur = points[route[0]-1]
        for idx in range(1, len(route)):
            nxt = points[route[idx]-1]
            # 행 이동
            dr = 1 if nxt[0] > cur[0] else -1
            for r in range(cur[0], nxt[0], dr):
                time_map[(t, (r, cur[1]))] += 1
                t += 1
            # 열 이동
            dc = 1 if nxt[1] > cur[1] else -1
            for c in range(cur[1], nxt[1], dc):
                time_map[(t, (nxt[0], c))] += 1
                t += 1
            cur = nxt
        time_map[(t, tuple(cur))] += 1  # 마지막 위치

    count = 0
    for v in time_map.values():
        if v >= 2:
            count += 1

    return count