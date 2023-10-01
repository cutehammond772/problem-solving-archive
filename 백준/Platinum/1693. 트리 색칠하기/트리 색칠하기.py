import sys, math
sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline().rstrip()
INF = 2 ** 63 - 1

def solve(N, adj):
	# 표현 가능한 최대 색깔의 수는 ceil(log2(N)) 개이다.
	colors = math.ceil(math.log2(N)) + 1
	memo = [[INF] * colors for _ in range(N + 1)]

	def traverse(prev, node):
		for next in adj[node]:
			if prev == next:
				continue

			traverse(node, next)
		
		# 각 루트 노드의 색깔에 대해 DP를 수행한다.
		for color in range(1, colors):
			memo[node][color] = color

			# 루트 노드의 하위 노드는 각각 독립적이므로, 가장 적은 비용을 선택한다. (루트 노드의 색 제외)
			for child in adj[node]:
				if prev == child:
					continue

				min_cost = INF

				for child_color in range(1, colors):
					if color == child_color:
						continue

					min_cost = min(min_cost, memo[child][child_color])

				memo[node][color] += min_cost

	traverse(0, 1)
	return min(memo[1])

if __name__ == "__main__":
	N = int(input())
	adj = [set() for _ in range(N + 1)]

	for _ in range(N - 1):
		P, Q = map(int, input().split())

		adj[P].add(Q)
		adj[Q].add(P)

	print(solve(N, adj))
