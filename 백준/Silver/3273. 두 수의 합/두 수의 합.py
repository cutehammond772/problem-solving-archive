import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A, X):
	result = 0
	p, q = 0, N - 1

	A.sort()

	while p < q:
		current = A[p] + A[q]

		if current == X:
			result += 1

		if current >= X: q -= 1
		else: p += 1

	return result

if __name__ == '__main__':
	N = int(input())
	A = [*map(int, input().split())]
	X = int(input())

	print(solve(N, A, X))
