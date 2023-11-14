import sys
from heapq import heapify, heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N, M = map(int, input().split())
	A = [*map(int, input().split())]
	B = [*map(int, input().split())]

	version = [0] * (N + M + 1)
	n_heap = [(A[x], 1 + x, version[1 + x]) for x in range(N)]
	m_heap = [(B[x], (N + 1) + x, version[(N + 1) + x]) for x in range(M)]

	heapify(n_heap)
	heapify(m_heap)

	K = int(input())

	for _ in range(K):
		C, *A = input().split()

		# 인구 수정하기
		if C == 'U':
			x, y = map(int, A)
			version[x] += 1

			if 1 <= x <= N:
				heappush(n_heap, (y, x, version[x]))

			elif N + 1 <= x <= N + M:
				heappush(m_heap, (y, x, version[x]))

		# 최단 경로 출력
		elif C == 'L':
			n, m = 0, 0

			while n_heap:
				p, x, v = n_heap[0]
				n = x

				if version[x] == v:
					break

				heappop(n_heap)

			while m_heap:
				p, x, v = m_heap[0]
				m = x

				if version[x] == v:
					break

				heappop(m_heap)

			print(n, m)
