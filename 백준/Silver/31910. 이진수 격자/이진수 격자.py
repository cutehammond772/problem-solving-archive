import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	N = int(input())
	result = 0

	matrix = [[*map(int, input().split())] for _ in range(N)]
	memo = [[0] * N for _ in range(N)]

	for row in range(N):
		for col in range(N):
			# 현재 위치
			memo[row][col] = matrix[row][col]

			# 위쪽에서 아래쪽으로
			if row > 0:
				memo[row][col] = max(memo[row][col], matrix[row][col] + (memo[row - 1][col] << 1))

			# 왼쪽에서 오른쪽으로
			if col > 0:
				memo[row][col] = max(memo[row][col], matrix[row][col] + (memo[row][col - 1] << 1))

			result = max(result, memo[row][col])

	print(result)
