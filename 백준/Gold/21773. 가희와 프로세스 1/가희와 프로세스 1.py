import sys
from heapq import heappush, heappop, heapify
input = lambda: sys.stdin.readline().rstrip()
MOD = int(1e9 + 7)

def solve(T, P):
	result, heap = [], [*P]

	# 우선순위 큐 초기화
	heapify(heap)

	for _ in range(T):
		priority, id, time = heappop(heap)

		result.append(id)
		time -= 1

		if time <= 0:
			continue

		heappush(heap, (priority + 1, id, time))

	return result

if __name__ == "__main__":
	T, N = map(int, input().split())
	P = []

	for _ in range(N):
		A, B, C = map(int, input().split())
		P.append((-C, A, B))

	print(*solve(T, P), sep='\n')
