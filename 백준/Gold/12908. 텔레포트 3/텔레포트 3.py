import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 10

if __name__ == '__main__':
	# (tp number, x, y)
	points = []

	xs, ys = map(int, input().split())
	xe, ye = map(int, input().split())

	points.append((-1, xs, ys))
	points.append((-1, xe, ye))

	for num in range(3):
		tx1, ty1, tx2, ty2 = map(int, input().split())

		points.append((num, tx1, ty1))
		points.append((num, tx2, ty2))

	P = len(points)
	matrix = [[INF] * P for _ in range(P)]

	for i in range(P - 1):
		for j in range(i + 1, P):
			t1, x1, y1 = points[i]
			t2, x2, y2 = points[j]

			# teleport
			if t1 == t2 >= 0:
				matrix[i][j] = matrix[j][i] = 10

			else:
				matrix[i][j] = matrix[j][i] = abs(x1 - x2) + abs(y1 - y2)

	for k in range(P):
		for i in range(P):
			for j in range(P):
				matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

	print(matrix[0][1])
