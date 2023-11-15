import sys, math
input = lambda: sys.stdin.readline().rstrip()

def combinations(A, C):
	L = len(A)
	result = []

	for bit in range(1 << L):
		total = 0

		for i in range(L):
			if bit & 1 << i:
				total += A[i]

		if total <= C:
			result.append(total)

	return result

def upper_bound(A, K):
	x, y = 0, len(A)

	while x < y:
		mid  = (x + y) >> 1

		if A[mid] > K:
			y = mid
		else:
			x = mid + 1

	return x

def solve(N, C, A):
	if N == 1:
		return 2 if A[0] <= C else 1

	P, Q = combinations(A[:(N // 2)], C), combinations(A[(N // 2):], C)

	# 한 쪽만 정렬한다.
	Q.sort()
	result = 0

	for amount in P:
		result += upper_bound(Q, C - amount)

	return result

if __name__ == '__main__':
	N, C = map(int, input().split())
	A = [*map(int, input().split())]

	print(solve(N, C, A))
