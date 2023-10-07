import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 10001

if __name__ == "__main__":
	N, K = map(int, input().split())
	coins = {int(input()) for _ in range(N)}

	memo = [INF] * (K + 1)
	memo[0] = 0

	for total in range(1, K + 1):
		for coin in coins:
			if total - coin >= 0:
				memo[total] = min(memo[total], memo[total - coin] + 1)

	print(memo[K] if memo[K] < INF else -1)
	