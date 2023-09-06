import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 2 ** 63 - 1

def solve(N, T, M, adj):
	result = INF
	visited = set()

	def traverse(node, lt, lm):
		nonlocal result

		if lm < 0 or lt < 0:
			return

		if node == N:
			result = min(result, M - lm)
			return

		for next, t, m in adj[node]:
			if next in visited:
				continue

			visited.add(next)
			traverse(next, lt - t, lm - m)
			visited.remove(next)

	traverse(1, T, M)
	return -1 if result == INF else result

if __name__ == '__main__':
	N = int(input())
	T, M = map(int, input().split())

	L = int(input())
	adj = [set() for _ in range(N + 1)]

	for _ in range(L):
		P, Q, t, m = map(int, input().split())
		adj[P].add((Q, t, m))
		adj[Q].add((P, t, m))

	print(solve(N, T, M, adj))
