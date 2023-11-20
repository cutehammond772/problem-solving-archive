import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, heavier, lighter):
	result = 0

	def find(graph, root):
		count = 0
		discover = [False] * (N + 1)
		queue = [root]

		discover[root] = True

		while queue:
			node = queue.pop()

			for next in graph[node]:
				if discover[next]:
					continue

				count += 1
				discover[next] = True
				queue.append(next)

		return count

	for node in range(1, N + 1):
		heavy, light = find(heavier, node), find(lighter, node)
		result += heavy > (N // 2) or light > (N // 2)

	return result

if __name__ == '__main__':
	N, M = map(int, input().split())
	heavier = [[] for _ in range(N + 1)]
	lighter = [[] for _ in range(N + 1)]

	for _ in range(M):
		a, b = map(int, input().split())

		heavier[b].append(a)
		lighter[a].append(b)

	print(solve(N, heavier, lighter))
