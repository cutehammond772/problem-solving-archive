import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 15001

def solve(N, matrix):
	result = [[] for _ in range(N)]

	for x in range(N - 1):
		for y in range(x + 1, N):
			check = True

			for k in range(N):
				if k == x or k == y:
					continue

				if matrix[x][y] == matrix[x][k] + matrix[k][y]:
					check = False
					break

			if check:
				result[x].append(y + 1)
				result[y].append(x + 1)

	return result

if __name__ == '__main__':
	N = int(input())
	matrix = [[INF] * N for _ in range(N)]

	for x in range(N - 1):
		data = [*map(int, input().split())]

		for y in range(x + 1, N):
			matrix[x][y] = matrix[y][x] = data[y - (x + 1)]

	for x in range(N):
		matrix[x][x] = 0

	result = solve(N, matrix)

	for x in range(N):
		result[x].sort()
		print(len(result[x]), *result[x])
