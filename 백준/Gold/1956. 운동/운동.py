import sys
input = lambda:sys.stdin.readline().rstrip()
INF = int(1e8)

if __name__ == '__main__':
	V, E = map(int, input().split())
	dist = [[INF] * V for _ in range(V)]

	for _ in range(E):
		a, b, c = map(int, input().split())
		dist[a - 1][b - 1] = c

	for k in range(V):
		for i in range(V):
			for j in range(V):
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

	result = min(dist[i][i] for i in range(V))

	print(result if result != INF else -1)
