import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(M, P):
	if M == 1:
		return 1

	memo = [1]
	offset, increasing = 0, False

	for i in range(1, M):
		# 1. 음이 동일한 경우
		if P[offset] == P[i]:
			continue

		# 2. 초기 설정
		if offset == 0:
			increasing = P[offset] < P[i]

			memo[-1] += 1
			offset = i
			continue

		# 3. 계속 증가 또는 감소
		if (P[offset] < P[i]) == increasing:
			memo[-1] += 1
			offset = i
			continue

		# 4. 패턴이 바뀌는 경우
		increasing = P[offset] < P[i]
		memo.append(2)
		offset = i

	return max(memo)

if __name__ == "__main__":
	M = int(input())
	P = [*map(int, input().split())]

	print(solve(M, P))
