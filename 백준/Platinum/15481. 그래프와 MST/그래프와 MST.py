import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
DEPTH = 20

def find(U, x):
	if U[x] == x:
		return U[x]
	
	nodes = [x]
	
	while U[nodes[-1]] != nodes[-1]:
		nodes.append(U[nodes[-1]])
	
	for node in nodes:
		U[node] = nodes[-1]
	
	return U[x]

def union(U, T, x, y):
	x, y = find(U, x), find(U, y)
	
	if T[x] <= T[y]:
		x, y = y, x
	
	U[y] = U[x]
	T[x] += T[y]

def solve(N, M, E):
	# MST
	tree = [[] for _ in range(N + 1)]
	unused = []
	
	U = [*range(N + 1)]
	T = [1] * (N + 1)
	
	default_cost, count = 0, 0
	
	E.sort()
	
	for W, i, A, B in E:
		if (count >= N - 1) or (find(U, A) == find(U, B)):
			unused.append((W, i, A, B))
			continue
		
		union(U, T, A, B)
		
		tree[A].append((B, W))
		tree[B].append((A, W))
		
		default_cost += W
		count += 1
	
	# LCA
	result = [default_cost] * M
	
	ancestor = [[0] * DEPTH for _ in range(N + 1)]
	level = [0] * (N + 1)
	max_edge = [[0] * DEPTH for _ in range(N + 1)]
	
	queue = deque([(0, 1, 0)])
	
	while queue:
		prev, node, cost = queue.popleft()
		ancestor[node][0], max_edge[node][0] = prev, cost
		
		for x in range(1, DEPTH):
			ancestor[node][x] = ancestor[ancestor[node][x - 1]][x - 1]
			max_edge[node][x] = max(max_edge[node][x - 1], max_edge[ancestor[node][x - 1]][x - 1])
		
		for next, next_cost in tree[node]:
			if prev == next:
				continue
			
			level[next] = level[node] + 1
			queue.append((node, next, next_cost))
	
	for W, i, A, B in unused:
		max_current = 0
		
		if level[A] < level[B]:
			A, B = B, A
		
		for x in range(DEPTH - 1, -1, -1):
			if level[ancestor[A][x]] < level[B]:
				continue
				
			max_current = max(max_current, max_edge[A][x])
			A = ancestor[A][x]
		
		if A == B:
			result[i] += W - max_current
			continue
		
		for x in range(DEPTH - 1, -1, -1):
			LA, LB = ancestor[A][x], ancestor[B][x]
			
			if LA == LB:
				continue
			
			max_current = max(max_current, max_edge[A][x], max_edge[B][x])
			A, B = LA, LB
		
		max_current = max(max_current, max_edge[A][0], max_edge[B][0])
		
		result[i] += W - max_current
	
	return result

if __name__ == '__main__':
	N, M = map(int, input().split())
	E = []
	
	for i in range(M):
		U, V, W = map(int, input().split())
		E.append((W, i, U, V))
	
	print(*solve(N, M, E), sep='\n')
