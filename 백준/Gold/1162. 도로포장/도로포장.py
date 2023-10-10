import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 10 + 1

def solve(N, K, adj):
	# memo[node][k] = (k개의 도로를 포장했을 때 최단 거리)
	memo = [[INF] * (K + 1) for _ in range(N + 1)]
	queue = []

	# 시작 지점 추가
	memo[1] = [0] * (K + 1)
	heappush(queue, (0, 0, 1))

	while queue:
		dist, k, node = heappop(queue)

		if node == N or memo[node][k] < dist:
			continue

		for next, cost in adj[node]:
			# 해당 도로를 포장할 경우
			if k + 1 <= K and memo[next][k + 1] > dist:
				for x in range(k + 1, K + 1):
					if memo[next][x] <= dist:
						break

					memo[next][x] = dist

				heappush(queue, (dist, k + 1, next))

			# 해당 도로를 포장하지 않을 경우
			if memo[next][k] > dist + cost:
				for x in range(k, K + 1):
					if memo[next][x] <= dist + cost:
						break

					memo[next][x] = dist + cost

				heappush(queue, (dist + cost, k, next))

	return min(memo[N])

if __name__ == "__main__":
	N, M, K = map(int, input().split())
	adj = [[] for _ in range(N + 1)]

	for _ in range(M):
		a, b, c = map(int, input().split())

		adj[a].append((b, c))
		adj[b].append((a, c))

	print(solve(N, K, adj))
