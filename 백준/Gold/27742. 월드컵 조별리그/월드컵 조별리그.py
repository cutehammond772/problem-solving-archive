import sys
input = lambda: sys.stdin.readline().rstrip()

def check(matrix, T):
	# [승점, 골득실, 다득점, 상대 전적]
	P = [[0, 0, 0, 4 - i] for i in range(4)]

	for a in range(4 - 1):
		for b in range(a + 1, 4):
			if matrix[a][b] == -1:
				unknown = (a, b)
				continue

			if matrix[b][a] == -1:
				unknown = (b, a)
				continue

			cmp = matrix[a][b] - matrix[b][a]

			if cmp > 0:
				P[a][0] += 3
				P[a][1] += cmp
				P[a][2] += matrix[a][b]

				P[b][1] += -cmp
				P[b][2] += matrix[b][a]
			elif cmp < 0:
				P[b][0] += 3
				P[b][1] += -cmp
				P[b][2] += matrix[b][a]

				P[a][1] += cmp
				P[a][2] += matrix[a][b]
			else:
				P[a][0] += 1
				P[a][2] += matrix[a][b]

				P[b][0] += 1
				P[b][2] += matrix[b][a]

	P.sort()

	for x in range(4):
		if 4 - P[x][3] == T:
			return x > 1

def solve(T, K, matrix, unknown):
	P, Q = 0, K
	a, b = unknown
	result = 10 ** 12 + 1

	while P <= Q:
		mid = (P + Q) // 2
		matrix[a][b] = mid

		if check(matrix, T):
			result = min(result, mid)
			Q = mid - 1
		else:
			P = mid + 1

	return result if result != 10 ** 12 + 1 else -1

if __name__ == "__main__":
	T, K = map(int, input().split())
	matrix = [[0] * 4 for _ in range(4)]
	unknown = (-1, -1)

	for row in range(4):
		data = [*map(int, input().split())]

		for col in range(4):
			if data[col] == -1:
				unknown = (row, col)
				continue

			matrix[row][col] = data[col]

	print(solve(T - 1, K, matrix, unknown))
