import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7

# 누적 DP와 고정된 값에 대한 DP를 동시에 관리한다.
def solve(N, X):
	# i번째 수를 k로 고정했을 때의 수열의 수
	memo = [[0] * 201 for _ in range(201)]

	# i번째까지의 수열이 최대 k인 (누적) 수열의 수
	accu = [[0] * 201 for _ in range(201)]

	# 비내림차순으로 정렬한다.
	X.sort()

	for i in range(1, N + 1):
		for x in range(1, X[i] + 1):
			memo[i][x] = max(1, accu[i - 1][x])
			accu[i][x] = memo[i][x] + accu[i][x - 1]

		# 각 수의 최대가 중간에 갭이 생길 때를 대비하여,
		# 이를 마지막 경우의 수로 채운다.
		for x in range(X[i] + 1, 201):
			accu[i][x] = accu[i][x - 1]

	return (accu[N][X[N]] * N) % MOD

if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		N = int(input())
		X = [0] + [*map(int, input().split())]
		print(solve(N, X))
