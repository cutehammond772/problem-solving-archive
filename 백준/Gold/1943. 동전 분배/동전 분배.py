import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 100001

def solve(N, money, total):
	# 돈의 총합이 홀수이면 정확히 반으로 나누는 것은 불가능하다.
	if total % 2:
		return 0

	L = total // 2
	memo = [INF] * (L + 1)

	# 0원은 항상 만들 수 있다.
	memo[0] = 0

	for x in range(1, N + 1):
		cost, amount = money[x]

		for m in range(cost, L + 1):
			if memo[m] < INF:
				memo[m] = 0
				continue

			if memo[m - cost] + 1 <= amount:
				memo[m] = memo[m - cost] + 1

	return 1 if memo[L] < INF else 0

if __name__ == "__main__":
	for _ in range(3):
		N = int(input())
		money, total = [None], 0

		for _ in range(N):
			cost, amount = map(int, input().split())

			money.append((cost, amount))
			total += cost * amount

		print(solve(N, money, total))