import sys
from heapq import heapify, heappop
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e6 + 1)

def find(U, x):
	if U[x] == x:
		return U[x]
	
	nodes = [x]
	
	while U[nodes[-1]] != nodes[-1]:
		nodes.append(U[nodes[-1]])
	
	for node in nodes:
		U[node] = nodes[-1]
	
	return U[x]

def union(U, x, y):
	x, y = find(U, x), find(U, y)
	
	if U[x] <= U[y]:
		U[y] = U[x]
	
	else:
		U[x] = U[y]

def solve(N, edges, S, E):
	G = [[] for _ in range(N + 1)]
	U = [*range(N + 1)]
	
	# MST
	count = 0
	heapify(edges)
	
	while edges and count < N - 1:
		weight, h1, h2 = heappop(edges)
		
		if find(U, h1) == find(U, h2):
			continue
		
		union(U, h1, h2)
		count += 1
		
		G[h1].append((h2, -weight))
		G[h2].append((h1, -weight))
	
	# BFS
	result = [INF] * (N + 1)
	queue = deque([(S, S)])
	
	while queue:
		prev, node = queue.popleft()
		
		for next, weight in G[node]:
			if prev == next:
				continue
			
			result[next] = min(result[next], min(result[node], weight))
			queue.append((node, next))
	
	return result[E] if result[E] < INF else 0

if __name__ == "__main__":
	N, M = map(int, input().split())
	S, E = map(int, input().split())
	
	# 다리
	edges = []
	
	for _ in range(M):
		h1, h2, k = map(int, input().split())
		edges.append((-k, h1, h2))
	
	print(solve(N, edges, S, E))
	