import heapq
def to_min(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m
def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x:x[0])
    rooms = []
    for start, end in book_time:
        s = to_min(start)
        e = to_min(end) + 10 #청소 10분 추가
        if rooms and rooms[0]<=s:
            heapq.heappop(rooms)
        heapq.heappush(rooms, e)
            
    return len(rooms)