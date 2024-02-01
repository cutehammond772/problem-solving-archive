import sys
input = lambda: sys.stdin.readline().rstrip()

# 홀수 정사각형의 개수는?
# 1. 한 변의 제곱이 "홀수"여야 한다.
# 2. 비스듬한 정사각형이 차지하는 (좌표축에 평행하는) 영역 또한 정사각형이다.
# 3. 이때, 2.의 영역의 한 변은 "무조건 홀수"이다. (피타고라스 정리로부터 증명 가능)
# -> 따라서, k >= 0에 대해 (2k + 1) x (2k + 1)의 정사각형의 개수를 구하되,
# 각 개수에 k + 1를 곱해야 한다. (이는 비스듬한 정사각형의 개수까지 반영된 것이다.)
def solve(N, M):
	result = 0
	
	# 0 ... k
	k = ((min(N, M) + 1) // 2) - 1
	
	# sigma 0 ... k (8k^3 - 4(N + M - 1)k^2 - 2(N + M - NM)k + NM)
	result += 8 * (k * (k + 1) // 2) ** 2
	result -= 4 * (N + M - 1) * (k * (k + 1) * (2 * k + 1) // 6)
	result -= 2 * (N + M - N * M) * (k * (k + 1) // 2)
	result += (N * M) * (k + 1)
	
	return result

if __name__ == "__main__":
	while (data := input()) != "0 0":
		N, M = map(int, data.split())
		print(solve(N, M))
	