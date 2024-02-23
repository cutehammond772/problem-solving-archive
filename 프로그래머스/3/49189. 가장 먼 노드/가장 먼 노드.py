from collections import deque

def solution(n, edge):
    answer = 0
    
    # 1. 그래프 형성
    graph = [[] for _ in range(n + 1)]
    
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    # 2. BFS를 통해 1번 노드와의 최단 거리 구하기
    queue = deque([1])
    distance = [0] * (n + 1)
    
    while queue:
        node = queue.popleft()
        
        for next in graph[node]:
            if distance[next] or next == 1:
                continue
            
            distance[next] = distance[node] + 1
            queue.append(next)
    
    max_distance = max(distance)
    answer = distance.count(max_distance)
    
    return answer