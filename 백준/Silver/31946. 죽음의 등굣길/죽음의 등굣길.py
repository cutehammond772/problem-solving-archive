import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

mr = [-1, 1, -1, 1]
mc = [1, -1, -1, 1]

def solve(N, M, X, matrix):
	checked = [[False] * M for _ in range(N)]
	queue = deque([])

	# 1행 1열
	checked[0][0] = True
	queue.append((0, 0, matrix[0][0]))

	while queue:
		row, col, color = queue.popleft()

		for dr in range(X + 1):
			for dc in range(X + 1):
				# Check 1
				if dr + dc > X or dr + dc == 0:
					continue

				for x in range(4):
					nrow, ncol = row + dr * mr[x], col + dc * mc[x]

					# Check 2
					if not (0 <= nrow < N and 0 <= ncol < M):
						continue

					# Check 3
					if checked[nrow][ncol] or matrix[nrow][ncol] != color:
						continue

					checked[nrow][ncol] = True
					queue.append((nrow, ncol, color))

	return checked[N - 1][M - 1]

if __name__ == "__main__":
	N, M = int(input()), int(input())
	matrix = [[*map(int, input().split())] for _ in range(N)]
	X = int(input())

	result = solve(N, M, X, matrix)
	print("ALIVE" if result else "DEAD")
