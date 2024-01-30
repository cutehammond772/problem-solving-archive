def find(U, x):
    if U[x] == x:
        return x
    
    route = [x]
    
    while U[route[-1]] != route[-1]:
        route.append(U[route[-1]])
    
    for node in route:
        U[node] = route[-1]
    
    return U[x]

def union(U, x, y):
    x, y = find(U, x), find(U, y)
    
    if U[x] <= U[y]:
        U[y] = U[x]
    
    else:
        U[x] = U[y]

def solution(n, costs):
    answer = 0
    edges = 0
    
    # Union-Find
    U = [*range(n)]
    
    # 건설 비용 오름차순으로 정렬
    costs.sort(key=lambda t: t[2])
    
    for x, y, cost in costs:
        # MST의 간선 개수는 n - 1개이다.
        if edges == n - 1:
            break
        
        x, y = find(U, x), find(U, y)
        
        if x == y:
            continue
        
        union(U, x, y)
        
        edges += 1
        answer += cost
    
    return answer