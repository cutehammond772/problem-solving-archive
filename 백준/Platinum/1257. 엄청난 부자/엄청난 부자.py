import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
INF = 2 ** 63 - 1

def solve(M, N, A):
	# 유니크 처리 후 정렬한다.
	A = [*sorted(set(A))]

	K, R = A[-1], M % A[-1]
	memo = [INF] * K

	queue = deque([(0, 0)])
	memo[0] = 0

	# 0-1 BFS
	while queue:
		num, dist = queue.popleft()

		if num == R:
			return dist + M // K

		for x in range(len(A) - 1):
			next_num = num + A[x]

			if next_num < K:
				if memo[next_num] <= dist + 1:
					continue

				memo[next_num] = dist + 1
				queue.append((next_num, dist + 1))

			# K를 넘어선 경우, "K를 지우고 (-1)" -> "A[x]를 추가 (+1)"한다고 생각한다.
			# K를 아무리 지워도 숫자가 10^9 이상이므로 널널하기 때문이다.
			else:
				next_num %= K

				if memo[next_num] <= dist:
					continue

				memo[next_num] = dist
				queue.appendleft((next_num, dist))

	return M

if __name__ == "__main__":
	M, N = int(input()), int(input())
	A = [*map(int, input().split())]

	print(solve(M, N, A))
