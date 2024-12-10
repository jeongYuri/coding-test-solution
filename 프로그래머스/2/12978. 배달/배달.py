from collections import deque, defaultdict
def solution(N, road, k):
    graph = defaultdict(list)
    for u, v, w in road:
        graph[u].append((v,w))
        graph[v].append((u,w))
        
        min_time =[float('inf')] * (N+1)
        min_time[1] = 0
        q = deque([(1,0)])
        
        while q:
            c_node, c_time = q.popleft()
            for n, t in graph[c_node]:
                n_time = c_time+t
                if n_time < min_time[n]:
                    min_time[n] = n_time
                    q.append((n,n_time))
    return sum(1 for time in min_time if time<=k)