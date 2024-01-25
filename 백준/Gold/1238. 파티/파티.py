import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

def dijkstra(N, G, S):
	memo = [INF] * (N + 1)
	
	heap = [(0, S)]
	memo[S] = 0
	
	while heap:
		dist, node = heappop(heap)
		
		if memo[node] < dist:
			continue
		
		for next, cost in G[node]:
			next_dist = memo[node] + cost
			
			if memo[next] <= next_dist:
				continue
			
			memo[next] = next_dist
			heappush(heap, (next_dist, next))
	
	return memo

def solve(N, X, G):
	dist = [dijkstra(N, G, node) for node in range(1, N + 1)]
	
	return max(dist[node - 1][X] + dist[X - 1][node] for node in range(1, N + 1))

if __name__ == "__main__":
	N, M, X = map(int, input().split())
	G = [[] for _ in range(N + 1)]
	
	for _ in range(M):
		P, Q, C = map(int, input().split())
		
		G[P].append((Q, C))
	
	print(solve(N, X, G))
	