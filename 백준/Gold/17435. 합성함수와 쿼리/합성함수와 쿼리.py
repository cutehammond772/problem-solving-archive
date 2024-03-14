import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	M = int(input())
	A = [0, *map(int, input().split())]

	F = [[0] * (M + 1) for _ in range(21)]

	for x in range(1, M + 1):
		F[0][x] = A[x]

	# 희소 배열
	for i in range(1, 21):
		for x in range(1, M + 1):
			F[i][x] = F[i - 1][F[i - 1][x]]

	Q = int(input())

	for _ in range(Q):
		N, X = map(int, input().split())
		result = X

		for i in range(20, -1, -1):
			if N >= (1 << i):
				result = F[i][result]
				N -= 1 << i

		print(result)
