import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 100001

def find(N, adj, node):
	dist = [INF] * N
	queue = [node]

	dist[node] = 0
	result = (0, node)

	while queue:
		current = queue.pop()

		for next in adj[current]:
			if dist[current] + 1 > dist[next]:
				continue

			dist[next] = dist[current] + 1
			queue.append(next)

			result = max(result, (dist[next], next))

	return result

def solve(N, adj):
	_, start = find(N, adj, 0)
	cost, end = find(N, adj, start)

	return cost // 2 + 1 if cost % 2 else cost // 2

if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		N = int(input())
		adj = [set() for _ in range(N)]

		for _ in range(N - 1):
			a, b = map(int, input().split())
			adj[a].add(b)
			adj[b].add(a)

		print(solve(N, adj))
