import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

def solve(N, K, S, T, G):
	memo = [[INF] * K for _ in range(N + 1)]
	heap = []
	
	# 시작점 설정
	memo[S][0] = 0
	heappush(heap, (0, S))
	
	while heap:
		current, node = heappop(heap)
		
		if memo[node][current % K] < current:
			continue
		
		for next, cost in G[node]:
			next_cost = current + cost
			
			if next_cost >= memo[next][next_cost % K]:
				continue
			
			memo[next][next_cost % K] = next_cost
			heappush(heap, (next_cost, next))
	
	return memo[T][0] if memo[T][0] < INF else "IMPOSSIBLE"

if __name__ == '__main__':
	N, M, K = map(int, input().split())
	S, T = map(int, input().split())
	
	G = [[] for _ in range(N + 1)]
	
	for _ in range(M):
		U, V, W = map(int, input().split())
		G[U].append((V, W))
	
	print(solve(N, K, S, T, G))
	