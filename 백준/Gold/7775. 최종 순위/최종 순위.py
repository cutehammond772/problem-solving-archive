import sys
input = lambda: sys.stdin.readline().rstrip()
WRONG = ["Wrong information"]

def solve(N, P, K, D):
	# Case 2. "D = 1"인 경우,
	# 모든 학생들의 점수를 먼저 똑같이 배분한 다음
	# 상위 K명의 학생들에 대해 남은 점수(0 이상)를 똑같이 분배
	# 할 수 있어야 한다.
	if D == 1:
		for x in range((P // N) + 1):
			rest = P - (N * x)

			if rest % K == 0:
				return ([x + rest // K] * K) + ([x] * (N - K))

		return WRONG

	# Case 3. "D > 1"인 경우,
	# 상위 K명의 학생들을 분별할 수 있는 최소한의 점수만 추가한 다음
	# 나머지 점수를 1등에게 몰아주면 된다.
	if P < (D * (D - 1) // 2):
		return WRONG

	result = [0] * N

	for x in range(D - 1):
		result[x] += ((D - 1) - x)

	result[0] += P - (D * (D - 1) // 2)
	return result

# 조건 1. 모든 학생의 점수의 합은 P
# 조건 2. 상위 K명의 점수 중 서로 다른 점수의 수는 D
if __name__ == "__main__":
	N, P, K, D = map(int, input().split())
	print(*solve(N, P, K, D), sep='\n')
