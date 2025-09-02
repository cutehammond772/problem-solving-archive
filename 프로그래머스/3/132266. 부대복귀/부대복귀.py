from heapq import heappush, heappop

INF = 100001

def dijkstra(N, graph, start):
    memo = [INF] * (N + 1)
    
    # 시작점
    memo[start] = 0
    heap = []
    
    for x in graph[start]:
        heappush(heap, (1, start, x))
        memo[x] = 1
        
    while heap:
        dist, p, q = heappop(heap)
        
        for r in graph[q]:
            if memo[r] <= dist + 1:
                continue
            
            memo[r] = dist + 1
            heappush(heap, (memo[r], q, r))
    
    return memo

def solution(n, roads, sources, destination):
    answer = []
    graph = [set() for _ in range(n + 1)]
    
    for p, q in roads:
        graph[p].add(q)
        graph[q].add(p)
    
    dist = dijkstra(n, graph, destination)
    
    for x in sources:
        if dist[x] == INF:
            answer.append(-1)
            continue
        
        answer.append(dist[x])
    
    return answer