import sys
from collections import deque
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
INF = 11

def analyse_country(N, M, original):
	id = 1

	matrix = [[0] * M for _ in range(N)]
	bridges = []

	for row in range(N):
		for col in range(M):
			# 빈 공간인 경우
			if not original[row][col]:
				continue

			# 이미 특정한 섬으로 식별된 경우
			if matrix[row][col]:
				continue

			# 새로운 섬 등록
			queue = deque([(row, col)])
			matrix[row][col] = id

			while queue:
				current_row, current_col = queue.popleft()

				for dir in range(4):
					nrow, ncol = current_row + dr[dir], current_col + dc[dir]

					# 범위를 벗어난 경우
					if not (0 <= nrow < N and 0 <= ncol < M):
						continue

					# 이미 특정한 섬으로 식별된 경우
					if matrix[nrow][ncol]:
						continue

					# 빈 공간으로 나온 경우
					if not original[nrow][ncol]:
						bridges.append((nrow, ncol, id, dir, 1))
						continue

					# 같은 섬 내부인 경우
					matrix[nrow][ncol] = id
					queue.append((nrow, ncol))

			id += 1

	return id - 1, matrix, bridges

def create_bridges(islands, matrix, bridges):
	adjacent = [[INF] * (islands + 1) for _ in range(islands + 1)]
	graph = [[] for _ in range(islands + 1)]

	queue = deque(bridges)

	while queue:
		row, col, id, dir, size = queue.popleft()
		nrow, ncol = row + dr[dir], col + dc[dir]

		# 범위를 벗어난 경우
		if not (0 <= nrow < N and 0 <= ncol < M):
			continue

		# 같은 섬끼리 연결된 경우
		if matrix[nrow][ncol] == id:
			continue

		# 다른 섬끼리 연결된 경우
		if matrix[nrow][ncol] and matrix[nrow][ncol] != id:
			# 다리 길이는 2 이상이어야 한다.
			if size < 2:
				continue

			op = matrix[nrow][ncol]
			adjacent[id][op] = adjacent[op][id] = min(adjacent[op][id], size)
			continue

		queue.append((nrow, ncol, id, dir, size + 1))

	for a in range(1, islands):
		for b in range(a + 1, islands + 1):
			dist = adjacent[a][b]

			if dist < INF:
				graph[a].append((b, dist))
				graph[b].append((a, dist))

	return graph

def min_distance(islands, graph):
	count, dist, nodes = 0, 0, {1}
	heap = []

	# 1번 노드를 시작으로 한다.
	for next, cost in graph[1]:
		heappush(heap, (cost, 1, next))

	while heap:
		cost, prev, node = heappop(heap)

		if node in nodes:
			continue

		count += 1
		dist += cost
		nodes.add(node)

		for next, cost in graph[node]:
			if next in nodes:
				continue

			heappush(heap, (cost, node, next))

	return dist if count == islands - 1 else -1

def solve(N, M, matrix):
	# 1. 나라에 존재하는 섬을 분석하여, 각각의 다리(의 시작점)를 찾는다.
	islands, matrix, bridges = analyse_country(N, M, matrix)

	if islands < 1:
		return -1

	# 2. 각각의 다리를 연결시켜, 섬 간 가장 짧은 다리(2 이상)만 그래프화한다.
	graph = create_bridges(islands, matrix, bridges)

	# 3. 최소 스패닝 트리를 이용하여 모든 섬을 잇는 다리의 최소 길이를 구한다.
	result = min_distance(islands, graph)

	return result

if __name__ == "__main__":
	N, M = map(int, input().split())
	matrix = [[*map(int, input().split())] for _ in range(N)]

	print(solve(N, M, matrix))
