import sys, math
input = lambda: sys.stdin.readline().rstrip()

# 1. 격자 무늬를 일자 무늬로 만든다.
# 2. 적은 색상 부분을 반전시킨다.
# 3. 이때, 짝수인 경우 색상의 비율은 동일하지만
# 홀수인 경우 더 작은 부분이 존재하므로 이를 고려한다.
if __name__ == "__main__":
	N, M = map(int, input().split())

	# 홀수, 짝수 모두 이런 식으로 커버가 가능하다.
	print((N // 2) + (M // 2))

	# 행 반전
	for row in range(2, N + 1, 2):
		print(row, 1, row, M)

	# 열 반전
	for col in range(2, M + 1, 2):
		print(1, col, N, col)
