import sys
input = lambda: sys.stdin.readline().rstrip()

def lower_bound(A, K):
	x, y = 0, len(A)

	while x < y:
		mid = (x + y) // 2

		if A[mid] >= K:
			y = mid

		else:
			x = mid + 1

	return x

def solve(N, A, B):
	I = [0] * (N + 1)

	for i in range(N):
		I[B[i]] = i

	for i in range(N):
		A[i] = I[A[i]]

	Q = []

	for i in range(N):
		if not Q or Q[-1] < A[i]:
			Q.append(A[i])
			continue

		Q[lower_bound(Q, A[i])] = A[i]

	return len(Q)

if __name__ == '__main__':
	N = int(input())
	A = [*map(int, input().split())]
	B = [*map(int, input().split())]

	print(solve(N, A, B))
