from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    total = len(jobs)
    
    # 요청 시점 순으로 정렬한다.
    jobs.sort(reverse=True)
    
    heap = []
    
    # 마지막 작업의 종료 시간
    end = 0
    
    while True:
        while jobs and jobs[-1][0] <= end:
            heappush(heap, jobs.pop()[::-1])
        
        if not heap and jobs:
            heappush(heap, jobs.pop()[::-1])
        
        if not heap:
            break
        
        time, req = heappop(heap)
        end = max(end, req) + time
        
        answer += end - req
    
    return answer // total