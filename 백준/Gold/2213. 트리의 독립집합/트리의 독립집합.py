import sys
sys.setrecursionlimit(10001)

input = lambda: sys.stdin.readline().rstrip()
SELECTED, UNSELECTED = 0, 1

def solve(N, P, T):
	memo = [[-1] * 2 for _ in range(N + 1)]
	nodes = [[[], []] for _ in range(N + 1)]

	def traverse(prev, node, status):
		if memo[node][status] != -1:
			return memo[node][status]

		result = 0

		if status == SELECTED:
			result = P[node]
			nodes[node][status].append(node)

		for next in T[node]:
			if prev == next:
				continue

			if status == SELECTED:
				result += traverse(node, next, UNSELECTED)
				nodes[node][status].extend(nodes[next][UNSELECTED])

			elif status == UNSELECTED:
				unselected = traverse(node, next, UNSELECTED)
				selected = traverse(node, next, SELECTED)

				if selected >= unselected:
					result += selected
					nodes[node][status].extend(nodes[next][SELECTED])

				else:
					result += unselected
					nodes[node][status].extend(nodes[next][UNSELECTED])

		memo[node][status] = result
		return result

	selected = traverse(0, 1, SELECTED)
	unselected = traverse(0, 1, UNSELECTED)

	if selected >= unselected:
		return selected, nodes[1][SELECTED]

	else:
		return unselected, nodes[1][UNSELECTED]

if __name__ == "__main__":
	N = int(input())
	P = [0, *map(int, input().split())]
	T = [[] for _ in range(N + 1)]

	for _ in range(N - 1):
		A, B = map(int, input().split())

		T[A].append(B)
		T[B].append(A)

	total, nodes = solve(N, P, T)
	nodes.sort()

	print(total)
	print(*nodes)
