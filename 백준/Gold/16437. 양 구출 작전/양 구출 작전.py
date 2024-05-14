import sys
sys.setrecursionlimit(131313)
input = lambda: sys.stdin.readline().rstrip()

def solve(G, A):
	def traverse(prev, node):
		for next in G[node]:
			if prev == next:
				continue

			traverse(node, next)
			A[node] += max(0, A[next])

	traverse(0, 1)
	return A[1]

if __name__ == "__main__":
	N = int(input())
	G = [[] for _ in range(N + 1)]

	# 양의 경우 (+), 늑대의 경우 (-)
	A = [0] * (N + 1)

	for i in range(2, N + 1):
		Ti, Ai, Pi = input().split()

		A[i] += int(Ai) * (1 if Ti == 'S' else -1)
		G[i].append(int(Pi))
		G[int(Pi)].append(i)

	print(solve(G, A))
