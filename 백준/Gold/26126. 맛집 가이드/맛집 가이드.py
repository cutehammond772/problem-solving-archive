import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K, P, Q):
	result, count, group = 0, 0, 0
	memo = [0] * (N + 1)

	for x in range(N):
		# 각 평론가의 순위를 그룹에 반영
		p, q = P[x], Q[x]
		count += 1

		if p != q:
			group += ((memo[p] ^ 1) + (memo[q] ^ 1)) - (memo[p] + memo[q])

			memo[p] ^= 1
			memo[q] ^= 1

		# 그룹의 크기가 K 이상이고 모두 겹치는 경우
		if not group and count >= K:
			count = 0
			result += 1

	return result

# 두 평론가 모두 "똑같은 크기로" "차례대로" 분할하여,
# 각 그룹에 포함된 숫자가 같도록 최소한으로 분할하면 된다.
if __name__ == "__main__":
	N, K = map(int, input().split())
	P = [*map(int, input().split())]
	Q = [*map(int, input().split())]

	print(solve(N, K, P, Q))
