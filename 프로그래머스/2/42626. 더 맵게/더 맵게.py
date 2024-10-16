import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K:
        if len(scoville)<2:
            return -1
        small = heapq.heappop(scoville)
        small2 = heapq.heappop(scoville)
        new_scoville = small + (small2*2)
        heapq.heappush(scoville,new_scoville)
        answer+=1
    return answer