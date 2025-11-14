import heapq
def solution(players, m, k):
    answer = 0
    heap = []
    for t,player in enumerate(players):
        n = player//m
        while heap and heap[0]<=t:
            heapq.heappop(heap)
        cur = len(heap)
        if n>cur:
            add = n-cur
            answer+= add
            for _ in range(add):
                heapq.heappush(heap,t+k)
    return answer