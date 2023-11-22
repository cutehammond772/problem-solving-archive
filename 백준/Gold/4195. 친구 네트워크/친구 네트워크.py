import sys
input = lambda: sys.stdin.readline().rstrip()

def mapper():
	id = 0
	names = {}

	def get(name):
		nonlocal id

		if name not in names:
			names[name] = id
			id += 1

		return names[name]

	def total():
		return id

	return get, total

def find(U, x):
	if U[x] == x:
		return U[x]

	routes = [x]

	while U[routes[-1]] != routes[-1]:
		routes.append(U[routes[-1]])

	for route in routes:
		U[route] = routes[-1]

	return U[x]

def union(U, C, x, y):
	x, y = find(U, x), find(U, y)

	if U[x] == U[y]:
		return

	if U[x] <= U[y]:
		U[y] = U[x]
		C[x] += C[y]

	else:
		U[x] = U[y]
		C[y] += C[x]

def solve(N, Q):
	U, C = [*range(N)], [1] * N
	result = []

	for f1, f2 in Q:
		f1, f2 = find(U, f1), find(U, f2)

		union(U, C, f1, f2)
		result.append(C[find(U, f1)])

	return result

if __name__ == '__main__':
	T = int(input())

	for _ in range(T):
		F = int(input())
		get, total = mapper()
		Q = []

		for _ in range(F):
			f1, f2 = map(get, input().split())
			Q.append((f1, f2))

		print(*solve(total(), Q), sep='\n')
