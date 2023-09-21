import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A, S):
	# 빈 배열이면 그대로 반환한다.
	if not A:
		return A

	candidates = [(A[x], x) for x in range(N)]
	candidates.sort(reverse=True)

	for num, idx in candidates:
		if S >= idx:
			return [num] + solve(N - 1, A[:idx]+A[(idx + 1):], S - idx)

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	S = int(input())

	print(*solve(N, A, S))
