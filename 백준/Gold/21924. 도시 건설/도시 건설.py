import sys
from heapq import heapify, heappop
input = lambda: sys.stdin.readline().rstrip()

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

	if U[x] <= U[y]:
		U[y] = U[x]

	else:
		U[x] = U[y]

def solve(N, edges):
	U = [*range(N + 1)]
	count, result = 0, 0

	heapify(edges)

	while edges and count < N - 1:
		cost, a, b = heappop(edges)

		if find(U, a) == find(U, b):
			continue

		union(U, a, b)

		count += 1
		result += cost

	return result if count == N - 1 else -1

if __name__ == '__main__':
	N, M = map(int, input().split())

	total = 0
	edges = []

	for _ in range(M):
		a, b, c = map(int, input().split())
		edges.append((c, a, b))

		total += c

	result = solve(N, edges)

	if result == -1:
		print(-1)

	else:
		print(total - result)
