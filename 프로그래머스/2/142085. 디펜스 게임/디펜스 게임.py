import heapq
def solution(n, k, enemy):
    round = 0
    heap = []
    for idx, e in enumerate(enemy):
        heapq.heappush(heap,-e) 
        round += e
        
        if round>n:
            if k==0:
                return idx
            else:
                k-=1
                round+= heapq.heappop(heap)
                
            
        
    return len(enemy)