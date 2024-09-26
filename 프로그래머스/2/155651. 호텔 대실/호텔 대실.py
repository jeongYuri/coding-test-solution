import heapq
def time_to(time_str:str)->str:
    hh,mm = map(int,time_str.split(":"))
    return hh*60+mm
def solution(book_time:list)->int:
    cnt = 0
    book_time.sort(key=lambda x:x[0])
    heap=[]
    for start, end in book_time:
        start_time = time_to(start)
        end_time = time_to(end)+10 #청소 시간 10 분 추가
        if heap and start_time>=heap[0]:
            heapq.heappop(heap)
        else:
            cnt +=1
        heapq.heappush(heap, end_time)
    return cnt