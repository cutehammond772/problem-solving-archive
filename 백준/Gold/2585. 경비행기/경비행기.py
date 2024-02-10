import sys, math
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

def fuel(x1, y1, x2, y2):
	return math.ceil(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) / 10.0)

def solve(N, K, G):
	memo = [[INF] * (K + 1) for _ in range(N)]
	heap = []
	
	# 시작점 (S)
	memo[0] = [0] * (K + 1)
	
	for next, cost in G[0]:
		memo[next][1] = cost
		heappush(heap, (cost, next, 1))
		
	while heap:
		curr_cost, node, count = heappop(heap)
		
		if memo[node][count] < curr_cost:
			continue
		
		# K개의 정점까지만 이동 가능
		if count + 1 > K:
			continue
		
		for next, cost in G[node]:
			cost = max(cost, curr_cost)
			
			if memo[next][count + 1] <= cost:
				continue
			
			for x in range(count + 1, K + 1):
				memo[next][x] = min(memo[next][x], cost)
			
			heappush(heap, (cost, next, count + 1))
	
	# 도착점 (T)
	return min(memo[1])

if __name__ == "__main__":
	N, K = map(int, input().split())
	G = [[] for _ in range(N + 2)]
	
	# 모든 정점
	D = [(0, 0), (10000, 10000)]
	
	for _ in range(N):
		x, y = map(int, input().split())
		D.append((x, y))
	
	for p in range(N + 1):
		for q in range(p + 1, N + 2):
			cost = fuel(*D[p], *D[q])
			
			G[p].append((q, cost))
			G[q].append((p, cost))
	
	print(solve(N + 2, K + 1, G))
	