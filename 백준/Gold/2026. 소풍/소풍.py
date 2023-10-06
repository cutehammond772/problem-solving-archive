import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(K, matrix, friends):
	stack, result = [], None
	F = len(friends)

	def traverse(off):
		nonlocal stack, result

		# K명이 뽑힌 경우 모두 친구 사이이다.
		if len(stack) == K:
			result = stack[:]
			return

		for x in range(off, F):
			if result:
				return

			student = friends[x]

			if len(stack):
				check = True

				for friend in stack:
					if not matrix[student][friend]:
						check = False
						break

				if not check:
					continue

			stack.append(friends[x])
			traverse(off + 1)
			stack.pop()

	traverse(0)

	if not result:
		return [-1]

	return result

if __name__ == "__main__":
	K, N, F = map(int, input().split())

	matrix = [[False] * (N + 1) for _ in range(N + 1)]
	relation = [0] * (N + 1)

	for _ in range(F):
		P, Q = map(int, input().split())

		matrix[P][Q] = matrix[Q][P] = True
		relation[P] += 1
		relation[Q] += 1

	candidate = [x for x in range(1, N + 1) if relation[x] >= K - 1]
	print(*solve(K, matrix, candidate), sep='\n')
