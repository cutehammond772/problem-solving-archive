import sys
from heapq import heapify, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = 1 << 31

def find(U, x):
	if U[x] == x:
		return U[x]

	routes = [x]

	while U[routes[-1]] != routes[-1]:
		routes.append(U[routes[-1]])

	for route in routes:
		U[route] = routes[-1]

	return U[x]

def union(U, x, y):
	x, y = find(U, x), find(U, y)

	if x <= y:
		U[y] = U[x]

	else:
		U[x] = U[y]

if __name__ == '__main__':
	while data := input():
		M, N = map(int, data.split())

		if M == N == 0:
			break

		total, cost = 0, 0

		U = [*range(M + 1)]
		edges = []

		for _ in range(N):
			x, y, z = map(int, input().split())

			total += z
			edges.append((z, x, y))

		count = 0
		heapify(edges)

		while count < M - 1:
			z, x, y = heappop(edges)

			if find(U, x) == find(U, y):
				continue

			union(U, x, y)

			cost += z
			count += 1

		print(total - cost)
