import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	result = []
	A.sort()

	checked = [False] * N
	count = 0

	while count < N:
		for i in range(N):
			if checked[i]:
				continue

			if result and A[i] - result[-1] == 1:
				continue

			candidates = {A[x] for x in range(N) if not checked[x]}

			if candidates == {A[i], A[i] + 1}:
				continue

			checked[i] = True
			result.append(A[i])
			count += 1

			break

	return result

if __name__ == '__main__':
	N = int(input())
	A = [*map(int, input().split())]

	print(*solve(N, A))
