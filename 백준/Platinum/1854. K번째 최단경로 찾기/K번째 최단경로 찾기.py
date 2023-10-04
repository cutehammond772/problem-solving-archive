import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K, adj):
	queue = []
	result = [-1] * (N + 1)
	order = [[] for _ in range(N + 1)]
	
	heappush(queue, (0, 1))

	while queue:
		distance, node = heappop(queue)

		if len(order[node]) >= K:
			continue

		order[node].append(distance)

		for next, cost in adj[node]:
			next_distance = distance + cost
			heappush(queue, (next_distance, next))

	for x in range(1, N + 1):
		if len(order[x]) < K:
			continue

		order[x].sort()
		result[x] = order[x][K - 1]

	return result[1:]

if __name__ == "__main__":
	N, M, K = map(int, input().split())
	adj = [set() for _ in range(N + 1)]

	for _ in range(M):
		a, b, c = map(int, input().split())
		adj[a].add((b, c))

	print(*solve(N, K, adj), sep='\n')
