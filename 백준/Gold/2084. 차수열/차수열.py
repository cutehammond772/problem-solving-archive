import sys
from heapq import heappush, heappop, heapify
input = lambda: sys.stdin.readline().rstrip()

def solve(N, D):
	# Case 1. 차수의 합은 항상 짝수여야 한다.
	if sum(D) % 1:
		return [[-1]]

	# Case 2. 간선의 최대 개수는 COMB(N, 2)이다.
	if N * (N - 1) < sum(D):
		return [[-1]]

	# Case 3.
	matrix = [[0] * N for _ in range(N)]
	heap = [(-D[i], i) for i in range(N)]
	heapify(heap)

	while heap:
		last, p = heappop(heap)
		last *= -1
		candidates = []

		while last and heap:
			another, q = heappop(heap)
			last -= 1

			if another + 1:
				candidates.append((another + 1, q))

			matrix[p][q] = matrix[q][p] = 1

		if last:
			return [[-1]]

		while candidates:
			heappush(heap, candidates.pop())

	return matrix

if __name__ == "__main__":
	N = int(input())
	D = [*map(int, input().split())]

	matrix = solve(N, D)
	for row in matrix:
		print(*row)
