import sys
from heapq import heapify, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = 1e7

def dist(P, Q):
	xp, yp = P
	xq, yq = Q

	return ((xp - xq) ** 2 + (yp - yq) ** 2) ** 0.5

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
	N, M = map(int, input().split())
	P = [(INF, INF)]
	U = [*range(N + 1)]

	for _ in range(N):
		X, Y = map(int, input().split())
		P.append((X, Y))

	for _ in range(M):
		A, B = map(int, input().split())
		union(U, A, B)

	edges = []

	for i in range(1, N):
		for j in range(i + 1, N + 1):
			edges.append((dist(P[i], P[j]), i, j))

	heapify(edges)
	result = 0.0

	while edges:
		d, i, j = heappop(edges)

		if find(U, i) == find(U, j):
			continue

		result += d
		union(U, i, j)

	print(f"{result:.2f}")
