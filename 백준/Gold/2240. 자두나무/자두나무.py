import sys
input = lambda: sys.stdin.readline().rstrip()

# 움직임 횟수가 (짝수 / 홀수)이면 위치는 (1번 / 2번)이다.
def solve(T, W, A):
	memo = [[0] * (W + 1) for _ in range(T + 1)]
	result = 0
	
	for t in range(1, T + 1):
		for w in range(0, W + 1):
			memo[t][w] = max(memo[t - 1][w], memo[t - 1][max(0, w - 1)]) + (A[t] == (w % 2) + 1)
			result = max(result, memo[t][w])
			
	return result

if __name__ == "__main__":
	T, W = map(int, input().split())
	A = [0] + [int(input()) for _ in range(T)]
	
	print(solve(T, W, A))
