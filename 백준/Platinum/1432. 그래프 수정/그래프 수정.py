import sys
from heapq import heappush, heappop, heapify
input = lambda: sys.stdin.readline().rstrip()

def solve(N, adj):
	result = [0] * N

	out_degree = [0] * N
	rev = [[] for _ in range(N)]

	for i in range(N):
		for j in range(N):
			if not matrix[i][j]:
				continue

			rev[j].append(i)
			out_degree[i] += 1

	heap = []
	count, num = 0, N

	for root in range(N):
		if out_degree[root] == 0:
			heappush(heap, -root)

	while heap:
		node = heappop(heap)

		result[-node] = num
		count += 1
		num -= 1

		for next in rev[-node]:
			out_degree[next] -= 1

			if out_degree[next] == 0:
				heappush(heap, -next)

	if count < N:
		return [-1]
	
	return result

if __name__ == "__main__":
	N = int(input())
	matrix = [[int(ch) for ch in input()] for _ in range(N)]

	print(*solve(N, matrix))
