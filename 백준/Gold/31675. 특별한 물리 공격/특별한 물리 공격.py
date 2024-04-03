import sys
input = lambda: sys.stdin.readline().rstrip()

# dp[n] = max(dp[n - 2] + R[n - 1], dp[n - 3] + R[n - 2] + R[n - 1])
def solve(N, R):
	memo = [0] * N

	memo[0] = 0

	if N > 1:
		memo[1] = R[0]

	if N > 2:
		memo[2] = R[1]

	for i in range(3, N):
		memo[i] = max(memo[i - 2] + R[i - 1], memo[i - 3] + (R[i - 2] + R[i - 1]))

	result = memo[-1]

	if N > 1:
		result = max(result, memo[-2] + R[-1])

	return result

if __name__ == "__main__":
	N = int(input())
	R = [*map(int, input().split())]

	print(solve(N, R))
