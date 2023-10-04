import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = 20001.0

def solve(N, adj):
	result = INF

	# 특정 정점을 시작점으로 하여 계산한다.
	for S in range(1, N + 1):
		queue = []

		dist = [INF] * (N + 1)
		dist[S] = 0

		heappush(queue, (0, S))

		while queue:
			distance, node = heappop(queue)

			for next, cost in adj[node]:
				# 자기 자신을 향하는 간선은 나중에 처리한다.
				if node == next:
					continue

				if dist[next] > distance + cost:
					dist[next] = distance + cost
					heappush(queue, (dist[next], next))

		ignition = 0.0

		for node in range(1, N + 1):
			for prev, cost in adj[node]:
				ignition = max(ignition, dist[node] + ((dist[prev] + cost) - dist[node]) / 2)

		result = min(result, ignition)

	return result

if __name__ == "__main__":
	N, M = map(int, input().split())
	adj = [set() for _ in range(N + 1)]

	for _ in range(M):
		S, E, L = map(int, input().split())

		adj[S].add((E, L))
		adj[E].add((S, L))

	print(solve(N, adj))
