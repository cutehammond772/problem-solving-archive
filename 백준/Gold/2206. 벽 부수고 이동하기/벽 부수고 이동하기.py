import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 6 + 1
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def traverse(N, M, A, wall, point):
	queue = deque([(*point, 1)])
	A[point[0]][point[1]] = 1

	while queue:
		row, col, dist = queue.popleft()

		for x in range(4):
			nrow, ncol = row + dr[x], col + dc[x]

			if not (0 <= nrow < N and 0 <= ncol < M):
				continue

			if A[nrow][ncol] <= dist + 1:
				continue

			if wall[nrow][ncol]:
				continue

			A[nrow][ncol] = dist + 1
			queue.append((nrow, ncol, dist + 1))

def solve(N, M, wall):
	S = [[INF] * M for _ in range(N)]
	E = [[INF] * M for _ in range(N)]

	traverse(N, M, S, wall, (0, 0))
	traverse(N, M, E, wall, (N - 1, M - 1))

	result = min(S[N - 1][M - 1], E[0][0])

	for row in range(N):
		for col in range(M):
			if not wall[row][col]:
				continue

			for a in range(4 - 1):
				for b in range(a + 1, 4):
					arow, acol = row + dr[a], col + dc[a]
					brow, bcol = row + dr[b], col + dc[b]

					if not (0 <= arow < N and 0 <= acol < M) or not (0 <= brow < N and 0 <= bcol < M):
						continue

					result = min(result, S[arow][acol] + E[brow][bcol] + 1, S[brow][bcol] + E[arow][acol] + 1)

	return -1 if result == INF else result

if __name__ == "__main__":
	N, M = map(int, input().split())
	matrix = [[int(c) for c in input()] for _ in range(N)]

	print(solve(N, M, matrix))
