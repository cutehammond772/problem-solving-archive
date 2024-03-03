import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e20)

def solve(N, G):
	memo = [[INF, INF] for _ in range(N + 1)]
	heap = []
	
	memo[1] = [0, INF]
	heappush(heap, (0, 1))
	
	while heap:
		current, node = heappop(heap)
		
		if memo[node][current % 2] < current:
			continue
		
		for next, cost in G[node]:
			next_cost = current + cost
			
			if next_cost >= memo[next][next_cost % 2]:
				continue
			
			memo[next][next_cost % 2] = next_cost
			heappush(heap, (next_cost, next))
	
	return memo

if __name__ == '__main__':
	N, M = map(int, input().split())
	G = [[] for _ in range(N + 1)]
	
	for _ in range(M):
		U, V, W = map(int, input().split())
		
		G[U].append((V, W))
		G[V].append((U, W))
	
	result = solve(N, G)
	
	for i in range(1, N + 1):
		even, odd = result[i]
		
		print(odd if odd < INF else -1, even if even < INF else -1)
