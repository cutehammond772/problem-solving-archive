import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

def dijkstra(N, from_graph, to_graph):
	memo = [INF] * N
	heap = []

	memo[0] = 0
	heappush(heap, (0, 0))

	while heap:
		dist, node = heappop(heap)

		if memo[node] < dist:
			continue

		for x in range(1, N):
			if (node - x >= 0) and memo[node - x] > dist + from_graph[x]:
				memo[node - x] = dist + from_graph[x]
				heappush(heap, (memo[node - x], node - x))

			if (node + x < N) and memo[node + x] > dist + to_graph[x]:
				memo[node + x] = dist + to_graph[x]
				heappush(heap, (memo[node + x], node + x))

	return memo

def solve(N, A):
	# 0 -> Node
	from_graph = [INF] * N

	# Node -> 0
	to_graph = [INF] * N

	# 1. 그래프 형성
	for d in range(1, N):
		if A[d]: from_graph[d] = A[d]
		if A[N - d]: to_graph[d] = A[N - d]

	# 2. 0을 기준으로 최단 거리 구하기
	from_zero, to_zero = dijkstra(N, from_graph, to_graph), dijkstra(N, to_graph, from_graph)

	return from_zero, to_zero

# u, v의 차를 통해 간선을 구하므로
# (u, v) -> (u - min(u, v), v - min(u, v))로 변환할 수 있다.
if __name__ == "__main__":
	N = int(input())
	A = [0, *map(int, input().split())]

	from_zero, to_zero = solve(N, A)

	Q = int(input())

	for _ in range(Q):
		a, b = map(int, input().split())

		# 최소를 0으로 변환
		a, b = a - min(a, b), b - min(a, b)

		if a:
			print(to_zero[a] if to_zero[a] < INF else -1)

		if b:
			print(from_zero[b] if from_zero[b] < INF else -1)

