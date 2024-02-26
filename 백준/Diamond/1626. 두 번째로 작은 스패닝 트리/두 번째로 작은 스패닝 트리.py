import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

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

def calculate(p, q):
	candidate = [*set(p + q)]
	candidate.sort(reverse=True)
	
	if len(candidate) == 1:
		return [*candidate, -1]
	
	return candidate[:2]

def solve(V, edges):
	# 트리
	G = [[] for _ in range(V + 1)]
	
	# Union Find
	U = [*range(V + 1)]
	T = [1] * (V + 1)
	
	# 최소 비용, 간선 카운트
	min_cost, count = 0, 0
	
	# 트리를 만들고 남은 간선들
	last_edges = []
	edges.sort()
	
	for C, A, B in edges:
		# 이미 트리가 형성된 경우
		if count >= V - 1:
			last_edges.append((C, A, B))
			continue
		
		# 사이클이 형성되는 경우
		if find(U, A) == find(U, B):
			last_edges.append((C, A, B))
			continue
		
		union(U, T, A, B)
		G[A].append((B, C))
		G[B].append((A, C))
		
		min_cost += C
		count += 1
	
	# 스패닝 트리나 두번째로 작은 스패닝 트리가 존재하지 않는 경우
	if count < V - 1 or not last_edges:
		return -1
	
	# memo[node][anc] = 조상 노드
	memo = [[0] * 20 for _ in range(V + 1)]
	
	# maxc[memo][anc] = 조상까지의 최대 간선 비용 (first_max, second_max)
	maxc = [[[0, 0] for _ in range(20)] for _ in range(V + 1)]
	
	# level[node] = 루트(1)을 기준으로 하는 트리의 레벨
	level = [0] * (V + 1)
	
	# (prev, node, cost)
	queue = deque([(0, 1, 0)])
	
	# 최종 결과
	result = 1 << 31
	
	while queue:
		prev, node, cost = queue.popleft()
		
		memo[node][0] = prev
		maxc[node][0] = [cost, -1]
		
		for anc in range(1, 20):
			memo[node][anc] = memo[memo[node][anc - 1]][anc - 1]
			maxc[node][anc] = calculate(maxc[node][anc - 1], maxc[memo[node][anc - 1]][anc - 1])
		
		for next, next_cost in G[node]:
			if prev == next:
				continue
			
			level[next] = level[node] + 1
			queue.append((node, next, next_cost))
	
	for C, A, B in last_edges:
		candidate = [-1, -1]
		
		# 1. 레벨 맞추기
		if level[A] < level[B]:
			A, B = B, A
		
		for x in range(19, -1, -1):
			if level[A] - (1 << x) >= level[B]:
				candidate = calculate(candidate, maxc[A][x])
				A = memo[A][x]
		
		# 2. LCA 찾기
		if A == B:
			if C > candidate[0]:
				result = min(result, min_cost + (C - candidate[0]))
			
			elif candidate[1] >= 0:
				result = min(result, min_cost + (C - candidate[1]))
				
			continue
			
		for x in range(19, -1, -1):
			LA, LB = memo[A][x], memo[B][x]
			
			if LA == LB:
				continue
			
			candidate = calculate(candidate, calculate(maxc[A][x], maxc[B][x]))
			A, B = LA, LB
		
		candidate = calculate(candidate, calculate(maxc[A][0], maxc[B][0]))
		
		if C > candidate[0]:
			result = min(result, min_cost + (C - candidate[0]))
		
		elif candidate[1] >= 0:
			result = min(result, min_cost + (C - candidate[1]))
	
	return result if result < (1 << 31) else -1

if __name__ == '__main__':
	V, E = map(int, input().split())
	edges = []
	
	for _ in range(E):
		A, B, C = map(int, input().split())
		edges.append((C, A, B))
	
	print(solve(V, edges))
		