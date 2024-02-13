import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

def solve(N, G, C):
	count, last = 0, 0
	memo = [INF] * (N + 1)
	
	# dijkstra
	heap = [(0, C)]
	memo[C] = 0
	
	while heap:
		time, node = heappop(heap)
		
		if memo[node] < time:
			continue
		
		count += 1
		last = max(last, time)
		
		for next, cost in G[node]:
			if time + cost >= memo[next]:
				continue
				
			memo[next] = time + cost
			heappush(heap, (time + cost, next))
	
	return count, last

if __name__ == "__main__":
	T = int(input())
	
	for _ in range(T):
		N, D, C = map(int, input().split())
		G = [[] for _ in range(N + 1)]
		
		for _ in range(D):
			A, B, S = map(int, input().split())
			G[B].append((A, S))
		
		print(*solve(N, G, C))
		