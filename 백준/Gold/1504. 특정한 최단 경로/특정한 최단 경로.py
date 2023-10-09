import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

INF = 8000001

def dijkstra(N, adj, A, B):
	dist = [INF] * (N + 1)
	queue = []

	# 시작 정점 추가
	dist[A] = 0
	heappush(queue, (0, A))

	while queue:
		cur_dist, node = heappop(queue)

		for next, cost in adj[node]:
			if cur_dist + cost >= dist[next]:
				continue

			dist[next] = cur_dist + cost

			# 도착 정점일 시 추가 X
			if next != B:
				heappush(queue, (cur_dist + cost, next))

	return dist[B]

def solve(N, adj, V1, V2):
	start_v1 = dijkstra(N, adj, 1, V1)
	start_v2 = dijkstra(N, adj, 1, V2)

	v1_v2 = dijkstra(N, adj, V1, V2)

	v1_end = dijkstra(N, adj, V1, N)
	v2_end = dijkstra(N, adj, V2, N)

	result = min(INF, start_v1 + v1_v2 + v2_end, start_v2 + v1_v2 + v1_end)
	return result if result < INF else -1

if __name__ == "__main__":
	N, E = map(int, input().split())
	adj = [[] for _ in range(N + 1)]

	for _ in range(E):
		a, b, c = map(int, input().split())
		adj[a].append((b, c))
		adj[b].append((a, c))

	V1, V2 = map(int, input().split())
	print(solve(N, adj, V1, V2))
