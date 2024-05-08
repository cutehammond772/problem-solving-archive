import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)
MAX = 1000000

def solve(A, B):
	# chance를 사용하지 않은 경우
	memo = [INF] * (MAX + 1)

	# chance를 사용한 경우
	chanced = [INF] * (MAX + 1)

	memo[A] = 0

	for x in range(A, MAX + 1):
		if x + 1 <= MAX:
			memo[x + 1] = min(memo[x + 1], memo[x] + 1)
			chanced[x + 1] = min(chanced[x + 1], chanced[x] + 1)

		if x * 2 <= MAX:
			memo[x * 2] = min(memo[x * 2], memo[x] + 1)
			chanced[x * 2] = min(chanced[x * 2], chanced[x] + 1)

		if x * 10 <= MAX:
			chanced[x * 10] = min(chanced[x * 10], memo[x] + 1)

	return min(memo[B], chanced[B])

if __name__ == "__main__":
	A, B = map(int, input().split())

	print(solve(A, B))
