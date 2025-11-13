import heapq
def solution(n, works):
    works =[-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        max_heap = heapq.heappop(works)
        if max_heap==0:
            break
        heapq.heappush(works, max_heap+1)
    return sum(w*w for w in works)