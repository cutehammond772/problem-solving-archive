import sys, math
input = lambda: sys.stdin.readline().rstrip()
INF = 1000010

def solve(N, M, X, Y, Sm, Pm, Sv, Pv):
	low, high = 1, INF

	while low < high:
		mid = (low + high) // 2
		possible = True

		# 남은 예산
		last = M

		for i in range(N):
			need = (X[i] * mid) - Y[i]
			money = INF

			for j in range(math.ceil(need / Sm[i]) + 1):
				money = min(money, (Pm[i] * j) + math.ceil(max(0, need - Sm[i] * j) / Sv[i]) * Pv[i])

			if last < money:
				possible = False
				break

			last -= money

		if possible:
			low = mid + 1

		else:
			high = mid

	return low - 1

if __name__ == '__main__':
	N, M = map(int, input().split())
	X, Y, Sm, Pm, Sv, Pv = [[0] * N for _ in range(6)]

	for i in range(N):
		X[i], Y[i], Sm[i], Pm[i], Sv[i], Pv[i] = map(int, input().split())

	print(solve(N, M, X, Y, Sm, Pm, Sv, Pv))
