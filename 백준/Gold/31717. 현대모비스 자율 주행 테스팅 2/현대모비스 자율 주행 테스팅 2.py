import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e18)

def solve(M, K, A, T):
	memo = [None]

	for i in range(1, M + 1):
		L = len(T[i][0])  # 열의 길이
		memo.append([[[INF, INF] for _ in range(L)] for _ in range(2)])

		# 1. 초기 설정
		memo[i][0][0][0] = 0 if T[i][0][0] == '.' else INF
		memo[i][1][0][1] = 0 if T[i][1][0] == '.' else INF

		memo[i][0][0][1] = min(memo[i][0][0][1], memo[i][1][0][1] + 1) if T[i][0][0] == '.' else INF
		memo[i][1][0][0] = min(memo[i][1][0][0], memo[i][0][0][0] + 1) if T[i][1][0] == '.' else INF

		# 2. DP
		for start in range(2):
			for col in range(1, L):
				# 1. 직진
				for row in range(2):
					if T[i][row][col] == '#':
						continue

					memo[i][row][col][start] = min(memo[i][row][col][start], memo[i][row][col - 1][start] + 1)

				# 2. 차선 변경
				for row in range(2):
					if T[i][row][col] == '#':
						continue

					memo[i][row][col][start] = min(memo[i][row][col][start], memo[i][1 - row][col][start] + 1)

	result = [[*memo[A[1]][0][-1], *memo[A[1]][1][-1]]]

	for x in range(2, K + 1):
		result.append([*memo[A[x]][0][-1], *memo[A[x]][1][-1]])

		if T[A[x - 1]][0][-1] == T[A[x]][0][0] == '.':
			result[-1][0] += min(result[-2][0], result[-2][1]) + 1
			result[-1][2] += min(result[-2][0], result[-2][1]) + 1

		else:
			result[-1][0] = result[-1][2] = INF

		if T[A[x - 1]][1][-1] == T[A[x]][1][0] == '.':
			result[-1][1] += min(result[-2][2], result[-2][3]) + 1
			result[-1][3] += min(result[-2][2], result[-2][3]) + 1

		else:
			result[-1][1] = result[-1][3] = INF

	result = min(result[-1])

	return result if result < INF else -1

if __name__ == "__main__":
	M, K = map(int, input().split())
	A = [0, *map(int, input().split())]

	# 트랙 Input
	T = [None]

	for _ in range(M):
		T.append([input(), input()])

	print(solve(M, K, A, T))
