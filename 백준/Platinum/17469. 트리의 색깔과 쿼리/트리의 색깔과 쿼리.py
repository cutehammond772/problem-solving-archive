import sys
input = lambda: sys.stdin.readline().rstrip()

def find(roots, x):
	if roots[x] != x:
		routes = [x]

		while routes[-1] != roots[routes[-1]]:
			routes.append(roots[routes[-1]])

		for route in routes:
			roots[route] = routes[-1]

	return roots[x]

def union(roots, colors, x, y):
	x, y = find(roots, x), find(roots, y)

	# Small to Large Trick
	if len(colors[x]) >= len(colors[y]):
		colors[x] |= colors[y]
		roots[y] = x

	else:
		colors[y] |= colors[x]
		roots[x] = y

# 간선을 미리 제거한 후, 역순으로 쿼리를 처리한다.
def solve(N, colors, parents, queries, cut):
	roots = [x for x in range(N + 1)]

	for node in range(2, N + 1):
		if cut[node]:
			continue

		union(roots, colors, node, parents[node])

	queries.reverse()
	result = []

	for a, node in queries:
		if a == 1:
			union(roots, colors, node, parents[node])

		elif a == 2:
			result.append(len(colors[find(roots, node)]))

	return result[::-1]

if __name__ == "__main__":
	N, Q = map(int, input().split())
	colors = [set() for _ in range(N + 1)]

	# 부모 노드
	parents = [0] * (N + 1)

	for node in range(2, N + 1):
		parent = int(input())
		parents[node] = parent

	# 색상 초기화
	for node in range(1, N + 1):
		color = int(input())
		colors[node].add(color)

	# 쿼리 입력
	queries = []
	cut = [False] * (N + 1)

	for _ in range(N - 1 + Q):
		a, b = map(int, input().split())

		if a == 1:
			cut[b] = True

		queries.append((a, b))

	print(*solve(N, colors, parents, queries, cut), sep='\n')
