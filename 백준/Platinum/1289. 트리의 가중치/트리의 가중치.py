import sys
sys.setrecursionlimit(10 ** 5)

input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = 2 ** 63 - 1

# 루트 노드를 1로 했을 때의 기준이다.
def solve(N, adj):
	# 해당 노드를 루트로 하는 트리에서, 해당 노드를 (경유하지 않고) 포함하는 경로
	single = [0] * (N + 1)

	# 해당 노드를 포함, 경유 또는 서브트리의 경우의 수까지 모두 포함
	total = [0] * (N + 1)

	# 트리 순회를 위한 방문 처리
	checked = [INF] * (N + 1)
	nodeID = 0

	def traverse(node):
		nonlocal nodeID

		checked[node] = nodeID
		nodeID += 1

		for next, cost in adj[node]:
			if checked[next] < checked[node]:
				continue

			traverse(next)
			path = cost * (single[next] + 1)

			total[node] = (total[node] + total[next] + path * (single[node] + 1)) % MOD
			single[node] = (single[node] + path) % MOD

	traverse(1)
	return total[1]

if __name__ == "__main__":
	N = int(input())
	adj = [[] for _ in range(N + 1)]

	for _ in range(N - 1):
		A, B, W = map(int, input().split())

		adj[A].append((B, W))
		adj[B].append((A, W))

	print(solve(N, adj))
