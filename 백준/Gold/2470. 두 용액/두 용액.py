import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 2 ** 63 - 1

def solve(N, A):
	x, y = 0, N - 1
	A.sort()

	result = [INF, 0, 0]

	while x < y:
		result = min(result, [abs(A[x] + A[y]), A[x], A[y]])

		if A[x] + A[y] >= 0:
			y -= 1
		else:
			x += 1

	return result[1:]

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]

	print(*solve(N, A))
