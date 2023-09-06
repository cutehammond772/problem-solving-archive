import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def furthest_node(N, V, adj):
	visited = [False] * (V + 1)
	queue = deque([(N, 0)])

	result, dist = N, 0
	visited[N] = True

	while queue:
		node, accu = queue.popleft()

		for next, cost in adj[node]:
			if visited[next]:
				continue

			visited[next] = True
			queue.append((next, accu + cost))

			if dist < accu + cost:
				dist = accu + cost
				result = next

	return result, dist

def solve(V, adj):
	leaf, _ = furthest_node(1, V, adj)
	_, result = furthest_node(leaf, V, adj)

	return result

if __name__ == "__main__":
	V = int(input())
	adj = [set() for _ in range(V + 1)]

	for _ in range(V):
		P, *Y = map(int, input().split())

		for x in range(0, len(Y) - 1, 2):
			Q, cost = Y[x], Y[x + 1]
			adj[P].add((Q, cost))
			adj[Q].add((P, cost))

	print(solve(V, adj))
