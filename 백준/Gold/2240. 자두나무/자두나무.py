import sys
input = lambda: sys.stdin.readline().rstrip()
FIRST, SECOND = 0, 1
IMPOSSIBLE = int(-1e10)

def solve(T, W, A):
	memo = [[[0, 0] for _ in range(W + 1)] for _ in range(T + 1)]
	sums = [[0] * (T + 1), [0] * (T + 1)]
	
	for x in range(1, T + 1):
		sums[FIRST][x] = sums[FIRST][x - 1] + (A[x] == 1)
		sums[SECOND][x] = sums[SECOND][x - 1] + (A[x] == 2)
	
	result = 0
	
	for t in range(1, T + 1):
		# 아예 움직이지 않는 경우
		memo[t][0][FIRST] = sums[FIRST][t]
		
		# 맨 처음 1번 자두나무 아래에 위치하므로, 움직이지 않고 2번 위치에 머무르는 경우는 존재하지 않다.
		memo[t][0][SECOND] = IMPOSSIBLE
		
		result = max(result, memo[t][0][FIRST])
		
		# 1번 이상 움직이는 경우
		for w in range(1, W + 1):
			for x in range(1, t + 1):
				memo[t][w][FIRST] = max(memo[t][w][FIRST], memo[t - x][w - 1][SECOND] + (sums[FIRST][t] - sums[FIRST][t - x]))
				memo[t][w][SECOND] = max(memo[t][w][SECOND], memo[t - x][w - 1][FIRST] + (sums[SECOND][t] - sums[SECOND][t - x]))
				
			result = max(result, memo[t][w][FIRST], memo[t][w][SECOND])
	
	return result

# memo[t][w][up/down] = memo[t - x][w - 1][down/up] + sums[up/down][t - x + 1 ... t]
if __name__ == "__main__":
	T, W = map(int, input().split())
	A = [0] + [int(input()) for _ in range(T)]
	
	print(solve(T, W, A))
