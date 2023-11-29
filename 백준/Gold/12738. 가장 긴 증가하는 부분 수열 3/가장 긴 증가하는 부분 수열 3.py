import sys
input = lambda: sys.stdin.readline().rstrip()

def lower_bound(A, K):
	x, y = 0, len(A)

	while x < y:
		mid = (x + y) >> 1

		if A[mid] >= K:
			y = mid
		else:
			x = mid + 1

	return x

def solve(N, A):
	seq = []

	for i in range(N):
		if not seq or seq[-1] < A[i]:
			seq.append(A[i])
			continue

		seq[lower_bound(seq, A[i])] = A[i]

	return len(seq)

if __name__ == '__main__':
	N = int(input())
	A = [*map(int, input().split())]

	print(solve(N, A))
