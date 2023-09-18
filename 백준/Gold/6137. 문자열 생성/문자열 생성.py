import sys
input = lambda: sys.stdin.readline().rstrip()

# 1. 양 끝 문자를 비교하여 더 사전 순으로 먼저 오는 것을 택한다.
# 2. 양 끝 문자가 같을 때, 다음과 같은 케이스가 존재한다.
#
# Case 1. 그 다음 양 끝 문자들 중 하나라도 지금 문자보다 먼저인 경우
# - 그 두 문자를 비교하여 더 먼저인 쪽을 택해야 한다.
#
# Case 2. 그 다음 양 끝 문자들 모두 지금 문자보다 나중인 경우
# - 결국 현재 두 문자를 먼저 택하고 그 다음 나중 문자들을 택하게 된다.
#
# Case 3. 그 다음 문자들도 서로 같은 경우
# - 그 다음 다음 문자에 대해 Case 1, 2를 고려한다.
#
# 즉, 위의 케이스를 모두 고려하려면 다음 양 끝 문자들을 연속적으로 고려해야 한다.
def solve(N, S):
	result = ''
	x, y = 0, N - 1

	while x < y:
		ax, ay = x, y

		while ax < ay:
			if S[ax] != S[ay]:
				break

			ax += 1
			ay -= 1

		if S[ax] <= S[ay]:
			result += S[x]
			x += 1
		else:
			result += S[y]
			y -= 1

	if x == y:
		result += S[x]

	return [result[x:min(x + 80, N)] for x in range(0, N, 80)]

if __name__ == "__main__":
	N = int(input())
	S = [input() for _ in range(N)]

	# 80글자마다 새줄
	print(*solve(N, S), sep='\n')
