import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N, K = map(int, input().split())
	A = [*map(int, input().split())]

	result = accu = sum(A[:K])

	for i in range(K, N):
		accu += A[i] - A[i - K]
		result = max(result, accu)

	print(result)
	