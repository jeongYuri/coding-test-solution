import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    min_heap, max_heap = [], []
    visited = [False] * k 

    for i in range(k):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':  # 삽입
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            visited[i] = True
        else:  # 삭제
            if n == 1:  # 최대값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:  # 최소값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # 남은 최소/최대 정리
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
