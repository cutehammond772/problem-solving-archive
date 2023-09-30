import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	N, M = map(int, input().split())

	matrix = [[0] * (M + 1) for _ in range(N + 1)]
	memo = [[0] * (M + 1) for _ in range(M + 1)]

	for row in range(1, N + 1):
		data = [1 - int(x) for x in input()]

		for col in range(1, M + 1):
			matrix[row][col] = matrix[row][col - 1] + data[col - 1]

	result = 0

	for row in range(1, N + 1):
		for p in range(1, M + 1):
			for q in range(p, M + 1):
				col = matrix[row][q] - matrix[row][p - 1]

				# 부분 열이 모두 0으로 채워진 경우
				if col == (q - p) + 1:
					memo[p][q] = memo[p][q] + col
					result = max(result, memo[p][q])
				
				# 그렇지 않은 경우 초기화한다.
				else:
					memo[p][q] = 0

	print(result)
