import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(N, X):
	memo = [-1] * 1000001
	result = [0] * N

	for idx in range(N):
		memo[X[idx]] = idx

	X.sort()
	bound = max(X)

	for k1 in X:
		for k2 in range(k1, bound + 1, k1):
			if memo[k2] >= 0:
				result[memo[k1]] += 1
				result[memo[k2]] -= 1

	return result


if __name__ == '__main__':
	N = int(input())
	X = [*map(int, input().split())]

	print(*solve(N, X))
