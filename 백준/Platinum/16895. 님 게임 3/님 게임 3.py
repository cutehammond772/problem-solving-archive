import sys
input = lambda: sys.stdin.readline().rstrip()

# 돌을 하나 이상 제거한 상태가 0이 되도록 하면 된다.
def solve(N, P):
	# 누적 XOR
	left, right = [0] * (N + 2), [0] * (N + 2)

	for x in range(1, N + 1):
		left[x] = left[x - 1] ^ P[x]
		right[(N + 1) - x] = right[(N + 1) - (x - 1)] ^ P[(N + 1) - x]

	result = 0

	# 각각의 돌더미에서 1개 이상 뺄 수 있는지에 대한 여부를 확인한다.
	for x in range(1, N + 1):
		num, other = P[x], left[x - 1] ^ right[x + 1]
		result += num > other

	return result

if __name__ == "__main__":
	N = int(input())
	P = [0, *map(int, input().split())]

	print(solve(N, P))
