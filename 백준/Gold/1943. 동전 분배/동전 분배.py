import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 10000000000001

def solve(N, money, total):
	# 돈의 총합이 홀수이면 정확히 반으로 나누는 것은 불가능하다.
	if total % 2:
		return 0

	L = total // 2
	memo = [[INF] * (L + 1) for _ in range(N + 1)]

	# 0원은 항상 만들 수 있다.
	memo[0][0] = 0

	for x in range(1, N + 1):
		cost, amount = money[x]

		for m in range(L + 1):
			if memo[x - 1][m] < INF:
				memo[x][m] = 0
				continue

			if m >= cost and memo[x][m - cost] + 1 <= amount:
				memo[x][m] = memo[x][m - cost] + 1

	return 1 if memo[N][L] < INF else 0

if __name__ == "__main__":
	for _ in range(3):
		N = int(input())

		money, total = [None], 0
		for _ in range(N):
			cost, amount = map(int, input().split())

			money.append((cost, amount))
			total += cost * amount

		print(solve(N, money, total))