import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	memo = [0] * N

	for x in range(N - 1):
		for y in range(x + 1, N):
			valid = True

			for k in range(x + 1, y):
				if A[k] >= A[x] + ((A[y] - A[x]) / (y - x)) * (k - x):
					valid = False
					break

			if valid:
				memo[x] += 1
				memo[y] += 1

	return max(memo)

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]

	print(solve(N, A))
