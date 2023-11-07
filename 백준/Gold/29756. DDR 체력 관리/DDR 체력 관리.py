import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N, K = map(int, input().split())

	S = [0, *map(int, input().split())]
	H = [0, *map(int, input().split())]

	# memo[phase][체력] = 점수
	memo = [[0] * 101 for _ in range(N + 1)]

	for x in range(1, N + 1):
		s, h = S[x], H[x]

		# 체력 회복
		for y in range(101):
			memo[x][min(100, y + K)] = max(memo[x - 1][y], memo[x][min(100, y + K)])

		# 춤추기
		for y in range(h, 101):
			memo[x][y - h] = max(memo[x][y - h], memo[x][y] + s)

	print(max(memo[-1]))
