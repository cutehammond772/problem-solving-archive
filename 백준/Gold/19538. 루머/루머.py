import sys, math
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, P, graph):
	# 최종 결과
	result = [-1] * (N + 1)

	# 루머를 믿는 주변인 수
	degrees = [0] * (N + 1)
	queue = deque([*P])

	for node in P:
		result[node] = 0

	# 위상 정렬 활용
	while queue:
		node = queue.popleft()

		for next in graph[node]:
			if result[next] >= 0:
				continue

			degrees[next] += 1

			if degrees[next] * 2 >= len(graph[next]):
				result[next] = result[node] + 1
				queue.append(next)

	return result[1:]

if __name__ == '__main__':
	N = int(input())
	graph = [set() for _ in range(N + 1)]

	for node in range(1, N + 1):
		adjacent = [*map(int, input().split())]

		for next in adjacent:
			if next == 0:
				break

			graph[node].add(next)
			graph[next].add(node)

	M = int(input())
	P = [*map(int, input().split())]

	print(*solve(N, M, P, graph))
