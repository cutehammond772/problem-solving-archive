import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10007

def pow(x, k):
	result = 1

	while k:
		if k & 1:
			result = (result * x) % MOD

		x *= x
		k >>= 1

	return result

def solve(N):
	threes, remainder = N // 3, N % 3

	# Case 1. 2 이하인 경우 그대로 반환하는 것이 최대이다.
	if not threes:
		return remainder

	# Case 2. 나머지가 없는 경우 3을 모두 곱하면 된다.
	if remainder == 0:
		return pow(3, threes) % MOD

	# Case 3. 나머지가 1인 경우 3을 하나 가져와 2 * 2를 만드는 것이 더 크다.
	if remainder == 1:
		return (pow(3, threes - 1) * 4) % MOD

	# Case 4. 나머지가 2인 경우 그대로 곱한다.
	return (pow(3, threes) * 2) % MOD

if __name__ == "__main__":
	N = int(input())
	print(solve(N))
