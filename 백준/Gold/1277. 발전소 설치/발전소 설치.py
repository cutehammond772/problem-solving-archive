import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = 2 ** 63 - 1

def distance(P, Q):
	x1, y1 = P
	x2, y2 = Q

	return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def solve(N, adj, dist):
	memo_dist = [INF] * (N + 1)
	heap = [(0.0, 1)]
	memo_dist[1] = 0.0

	while heap:
		accu, node = heappop(heap)

		for next in adj[node]:
			cost = dist[node][next]

			if accu + cost >= memo_dist[next]:
				continue

			memo_dist[next] = accu + cost
			heappush(heap, (memo_dist[next], next))

	return int(memo_dist[N] * 1000.0)

if __name__ == "__main__":
	N, W = map(int, input().split())
	M = float(input())

	P = [(INF, INF)]
	adj = [set() for _ in range(N + 1)]
	dist = [[-1.0] * (N + 1) for _ in range(N + 1)]

	for _ in range(N):
		x, y = map(int, input().split())
		P.append((x, y))

	for _ in range(W):
		a, b = map(int, input().split())
		dist_ab = distance(P[a], P[b])

		adj[a].add(b)
		adj[b].add(a)

		dist[a][b] = dist[b][a] = 0.0

	for a in range(1, N):
		for b in range(a + 1, N + 1):
			dist_ab = distance(P[a], P[b])

			if dist_ab > M or (b in adj[a]):
				continue

			adj[a].add(b)
			adj[b].add(a)

			dist[a][b] = dist[b][a] = dist_ab

	print(solve(N, adj, dist))
