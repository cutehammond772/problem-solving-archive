import sys
input = lambda: sys.stdin.readline().rstrip()

def find(N, graph, root):
	count = 0
	visited = [False] * (N + 1)

	queue = [root]
	visited[root] = True

	while queue:
		node = queue.pop()

		for next in graph[node]:
			if visited[next]:
				continue

			count += 1
			visited[next] = True
			queue.append(next)

	return count

if __name__ == '__main__':
	N, M = int(input()), int(input())
	heavier = [[] for _ in range(N + 1)]
	lighter = [[] for _ in range(N + 1)]

	for _ in range(M):
		x, y = map(int, input().split())

		heavier[x].append(y)
		lighter[y].append(x)

	for node in range(1, N + 1):
		print((N - 1) - find(N, lighter, node) - find(N, heavier, node))