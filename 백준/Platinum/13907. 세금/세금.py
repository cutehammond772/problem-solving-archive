import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 10

def solve(N, K, S, D, adj, tax):
	# dist[node][edge]
	dist = [[INF] * N for _ in range(N + 1)]

	heap = []

	dist[S][0] = 0
	heappush(heap, (0, 0, S))

	while heap:
		path, edge, node = heappop(heap)

		if node == D:
			continue

		for next, cost in adj[node]:
			found_better = False

			for e in range(edge + 2):
				if dist[next][e] <= path + cost:
					found_better = True
					break

			if found_better:
				continue

			dist[next][edge + 1] = path + cost
			heappush(heap, (dist[next][edge + 1], edge + 1, next))

	result = [min(dist[D])]
	current_tax = 0

	for k in range(1, K + 1):
		current_tax += tax[k - 1]
		cost = INF

		for edge in range(N):
			cost = min(cost, dist[D][edge] + current_tax * edge)

		result.append(cost)

	return result

if __name__ == "__main__":
	N, M, K = map(int, input().split())
	S, D = map(int, input().split())

	adj = [[] for _ in range(N + 1)]

	for _ in range(M):
		a, b, w = map(int, input().split())

		adj[a].append((b, w))
		adj[b].append((a, w))

	tax = [int(input()) for _ in range(K)]
	result = solve(N, K, S, D, adj, tax)

	print(*result, sep='\n')
