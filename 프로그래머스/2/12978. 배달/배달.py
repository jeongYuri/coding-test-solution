import heapq
def solution(N, road, K):
    INF = float('inf')
    answer = 0
    graph = [[]for _ in range(N+1)]
    for a,b, cost in road:
        graph[a].append((b,cost))
        graph[b].append((a,cost))
    dist = [INF]*(N+1)
    dist[1] = 0
    pq = []
    heapq.heappush(pq,(0,1))
    while pq:
        cost, node = heapq.heappop(pq)
        if dist[node]<cost:
            continue
        for nxt, nxt_c in graph[node]:
            new_cost = cost+nxt_c
            if new_cost< dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq,(new_cost, nxt))
    ans = sum(1 for i in range(1, N+1) if dist[i] <= K)
    return ans
        
    