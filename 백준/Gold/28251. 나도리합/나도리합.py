import sys
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

def union(U, T, G, x, y):
	x, y = find(U, x), find(U, y)

	if U[x] <= U[y]:
		U[y] = U[x]

		G[x] += G[y] + T[y] * T[x]
		T[x] += T[y]

	else:
		U[x] = U[y]

		G[y] += G[x] + T[x] * T[y]
		T[y] += T[x]

if __name__ == '__main__':
	N, Q = map(int, input().split())

	# 각 그룹의 나도리의 합
	T = [0, *map(int, input().split())]

	# 그룹
	U = [*range(N + 1)]

	# 각 그룹의 전투력
	G = [0] * (N + 1)

	for _ in range(Q):
		a, b = map(lambda t: find(U, int(t)), input().split())

		# 동일한 그룹인 경우
		if a == b:
			print(G[U[a]])
			continue

		# 서로 다른 그룹인 경우
		union(U, T, G, a, b)

		group = find(U, a)
		print(G[group])