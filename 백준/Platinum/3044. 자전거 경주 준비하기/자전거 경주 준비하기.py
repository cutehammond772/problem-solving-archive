import sys
from collections import defaultdict, deque
UNDISCOVERED, PATH, NOT_A_PATH = 0, 1, 2

sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline().rstrip()

def solve(N, adj, routes):
	invalid = False

	# 1. "DFS"를 통해 대회 경로만 탐색한다.
	visited = [False] * (N + 1)

	# 이전에 발견된 경로를 다시 탐색하지 않도록 한다.
	discovered = [UNDISCOVERED] * (N + 1)

	# Cycle이 생기는 지점을 체크한다.
	cycle = [False] * (N + 1)

	# 대회 경로만 포함된 그래프이다.
	graph = [set() for _ in range(N + 1)]
	in_degrees = [0] * (N + 1)

	def find(node):
		nonlocal invalid

		visited[node] = True
		has_destination = node == 2

		for next in adj[node]:
			if visited[next]:
				cycle[next] = True
				continue

			find_destination = (discovered[next] == PATH) if discovered[next] else find(next)
			has_destination |= find_destination

			if find_destination:
				graph[node].add(next)
				in_degrees[next] += 1

		if cycle[node] and has_destination:
			invalid = True

		visited[node] = False
		discovered[node] = PATH if has_destination else NOT_A_PATH

		return has_destination

	# 시작 지점부터 도착 지점을 탐색한다.
	find(1)

	if invalid:
		return "inf"

	# 2. "위상 정렬 + DP"를 통해 가능한 모든 경로의 수를 계산한다.
	queue = deque([1])
	memo = [0] * (N + 1)
	memo[1] = 1

	while queue:
		node = queue.popleft()

		for next in graph[node]:
			memo[next] = memo[next] + memo[node] * routes[(node, next)]
			in_degrees[next] -= 1

			if in_degrees[next] == 0:
				queue.append(next)

	return str(memo[2])[-9:]

if __name__ == "__main__":
	N, M = map(int, input().split())

	# 인접 리스트는 unique한 경로를 나타낸다.
	adjacent = [set() for _ in range(N + 1)]

	# 동일한 경로의 수를 저장한다.
	routes = defaultdict(int)

	for _ in range(M):
		A, B = map(int, input().split())

		routes[(A, B)] += 1
		adjacent[A].add(B)

	print(solve(N, adjacent, routes))
