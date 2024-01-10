import heapq

def solution(operations):
    heap = []

    for op in operations:
        command, value = op.split()

        if command == "I":
            heapq.heappush(heap, int(value))
        elif command == "D" and value == "1":
            if heap:
                heap.remove(max(heap))
                heapq.heapify(heap)
        elif command == "D" and value == "-1":
            if heap:
                heapq.heappop(heap)

    if not heap:
        return [0, 0]
    else:
        return [max(heap), min(heap)]

