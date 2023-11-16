import sys
input = lambda: sys.stdin.readline().rstrip()

def zec(N):
	memo = [0, 1]
	fib = [1, 1]

	for x in range(2, N + 1):
		f = fib[-1] + fib[-2]

		if x == f:
			memo.append(f)
			fib.append(f)

		else:
			memo.append(memo[x - fib[-1]])

	return memo[N]

def nearest(N):
	result = [1, 1]

	while result[-1] <= N:
		result.append(result[-1] + result[-2])

	return result[-2]

def solve(N):
	offset = nearest(N)

	# 패배하는 위치
	if offset == N:
		return -1

	# 필요한 최소 구슬의 개수
	return zec(N - offset)

if __name__ == '__main__':
	N = int(input())
	print(solve(N))
