import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, P):
	result = 0
	ones_only = True

	for i in range(N):
		Pi = P[i]

		if Pi > 1:
			ones_only = False

		result ^= Pi

	# Case 1. 돌더미 당 각각 한 개씩만 있는 경우,
	# 돌더미의 수가 홀수이면 선공이 질 수밖에 없다.
	check_01 = ones_only and result

	# Case 2. 위의 케이스가 아닌 경우, 선공은 어떻게든
	# 위의 상태로 만들 수 있다.
	check_02 = not ones_only and not result

	return "cubelover" if (check_01 or check_02) else "koosaga"

if __name__ == "__main__":
	N = int(input())
	P = [*map(int, input().split())]

	print(solve(N, P))
