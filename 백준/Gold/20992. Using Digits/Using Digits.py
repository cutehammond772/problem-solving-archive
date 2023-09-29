import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

INF = 90001
dr, dc = [0, 1], [1, 0]

def solve(R, C, codes, lair):
	L = len(codes)

	# memo[r][c][code] : code만큼 써서 (x, y) 위치로 이동했을 때의 최소 누적
	memo = [[[INF] * (L + 1) for _ in range(C)] for _ in range(R)]

	# (row, col, code, result)
	queue = deque([(0, 0, 0, lair[0][0])])
	memo[0][0][0] = lair[0][0]

	while queue:
		row, col, code, result = queue.popleft()

		if (row, col) == (R - 1, C - 1):
			continue

		if result > memo[row][col][code] or result >= memo[R - 1][C - 1][-1]:
			continue

		for i in range(2):
			nrow, ncol = row + dr[i], col + dc[i]

			if 0 <= nrow < R and 0 <= ncol < C:
				next = result + lair[nrow][ncol]

				if memo[nrow][ncol][code] > next:
					for x in range(code, L + 1):
						if memo[nrow][ncol][x] <= next:
							break

						memo[nrow][ncol][x] = next

					queue.append((nrow, ncol, code, next))

			if code >= L:
				continue

			nrow, ncol = nrow + codes[code] * dr[i], ncol + codes[code] * dc[i]

			if 0 <= nrow < R and 0 <= ncol < C:
				next = result + lair[nrow][ncol]

				if memo[nrow][ncol][code + 1] > next:
					for x in range(code + 1, L + 1):
						if memo[nrow][ncol][x] <= next:
							break

						memo[nrow][ncol][x] = next

					queue.append((nrow, ncol, code + 1, next))

	return memo[R - 1][C - 1][-1]

if __name__ == "__main__":
	C, R = map(int, input().split())
	codes = [int(i) for i in input()]

	# 익숙한 배치로 바꾼다. 결과에는 영향이 없다.
	lair = [[int(col) for col in input()] for _ in range(R)]
	lair.reverse()

	print(solve(R, C, codes, lair))
