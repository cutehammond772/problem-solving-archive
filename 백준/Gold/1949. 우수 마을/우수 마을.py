import sys
sys.setrecursionlimit(10001)

input = lambda: sys.stdin.readline().rstrip()
SELECTED, UNSELECTED = 0, 1

def solve(N, P, T):
	memo = [[-1] * 2 for _ in range(N + 1)]

	def traverse(prev, node, status):
		if memo[node][status] != -1:
			return memo[node][status]

		result = P[node] if status == SELECTED else 0

		for next in T[node]:
			if prev == next:
				continue

			if status == SELECTED:
				result += traverse(node, next, UNSELECTED)

			# "우수 - 일반 - 일반 - 일반 - 우수" 가 존재한다고 생각할 수 있으나,
			# 최대값을 구하는 과정에서 중간의 일반은 우수 마을로 자동으로 배정된다.
			elif status == UNSELECTED:
				result += max(traverse(node, next, UNSELECTED), traverse(node, next, SELECTED))

		memo[node][status] = result
		return result

	# 루트 노드를 1로 하며, 우수 마을로 선택된 경우 / 선택되지 않은 경우를 따진다.
	return max(traverse(0, 1, SELECTED), traverse(0, 1, UNSELECTED))

if __name__ == "__main__":
	N = int(input())
	P = [0, *map(int, input().split())]
	T = [[] for _ in range(N + 1)]

	for _ in range(N - 1):
		A, B = map(int, input().split())

		T[A].append(B)
		T[B].append(A)

	print(solve(N, P, T))
