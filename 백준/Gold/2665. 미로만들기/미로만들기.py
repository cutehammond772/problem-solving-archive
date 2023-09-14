import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = 2 ** 63 - 1

def solve(N, adj, dist):
	memo = [INF] * N

	heap = [(0, 0)]
	memo[0] = 0

	while heap:
		accu, node = heappop(heap)

		for next in adj[node]:
			cost = dist[node][next]

			if accu + cost >= memo[next]:
				continue

			memo[next] = accu + cost
			heappush(heap, (memo[next], next))

	return memo[N - 1]

if __name__ == "__main__":
	N = int(input())
	dist = [[0] * (N * N) for _ in range(N * N)]
	adj = [[] for _ in range(N * N)]

	for row in range(N):
		data = [1 - int(x) for x in input()]
		dist.append(data)

		# 특정 정점에 대한 진입 간선만 저장한다.
		for col in range(N):
			node = row * N + col

			# 왼쪽으로부터 진입
			if col > 0:
				adj[node - 1].append(node)
				dist[node - 1][node] = data[col]

			# 오른쪽으로부터 진입
			if col < N - 1:
				adj[node + 1].append(node)
				dist[node + 1][node] = data[col]

			# 위쪽으로부터 진입
			if row > 0:
				adj[node - N].append(node)
				dist[node - N][node] = data[col]

			# 왼쪽으로부터 진입
			if row < N - 1:
				adj[node + N].append(node)
				dist[node + N][node] = data[col]

	print(solve(N * N, adj, dist))
