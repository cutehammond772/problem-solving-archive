from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while len(scoville) > 1:
        first, second = heappop(scoville), heappop(scoville)
        
        if first >= K:
            return answer
        
        heappush(scoville, first + second * 2)
        answer += 1
        
    if scoville[0] < K:
        return -1
    
    return answer