import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 20001

def solve(S):
	L = len(S)

	# 특정 위치의 문자에 대해 SET, 그 이후를 NEXT로 처리했을 때..
	memo = [INF] * L

	# 처음에는 SET 후 WRITE하는 방법밖에 없다.
	memo[0] = 2

	for x in range(1, L):
		for y in range(x):
			next_cost = 2 * (x - y - 1)

			if S[x] == S[y]:
				memo[x] = min(memo[x], memo[y] + next_cost + 1)
			else:
				memo[x] = min(memo[x], memo[y] + next_cost + 2)

	return memo[L - 1]

if __name__ == "__main__":
	S = input()
	print(solve(S))
