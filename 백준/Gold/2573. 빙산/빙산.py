import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

# "덩어리 개수 체크"와 "빙산 높이 감소"의 두 과정으로 나뉜다.
# [0..n년 째]: "덩어리 개수 체크" -> "빙산 높이 감소"
# 로부터, "덩어리 개수 체크" 에서 2 이상이면 n을 반환, 0이 나오면 0을 반환한다.
def solve(N, M, matrix):
	# 덩어리 개수 체크
	def get_blocks():
		visited = [[0] * M for _ in range(N)]
		queue = deque([])

		block_id = 1

		for row in range(N):
			for col in range(M):
				if visited[row][col] or not matrix[row][col]:
					continue

				visited[row][col] = block_id
				block_id += 1

				queue.append((row, col))

				while queue:
					r, c = queue.popleft()

					for x in range(4):
						nrow, ncol = r + dr[x], c + dc[x]

						if not (0 <= nrow < N and 0 <= ncol < M):
							continue

						if visited[nrow][ncol] or not matrix[nrow][ncol]:
							continue

						visited[nrow][ncol] = visited[r][c]
						queue.append((nrow, ncol))

		return block_id - 1

	# 빙산 높이 감소
	def decrease_height():
		diff = [[0] * M for _ in range(N)]

		for row in range(N):
			for col in range(M):
				count = 0

				if not matrix[row][col]:
					continue

				for x in range(4):
					nrow, ncol = row + dr[x], col + dc[x]

					if not (0 <= nrow < N and 0 <= ncol < M):
						continue

					if not matrix[nrow][ncol]:
						count += 1

				diff[row][col] = max(-matrix[row][col], -count)

		for row in range(N):
			for col in range(M):
				matrix[row][col] += diff[row][col]

	for x in range(10000):
		count = get_blocks()

		# 덩어리가 존재하지 않는 경우,
		# 아예 처음부터 존재하지 않았거나 두 덩어리로 분해되지 않고 한 번에 모두 녹은 경우이다.
		if count == 0:
			return 0

		if count > 1:
			return x

		decrease_height()

	return 0

if __name__ == "__main__":
	N, M = map(int, input().split())
	matrix = [[*map(int, input().split())] for _ in range(N)]

	print(solve(N, M, matrix))
