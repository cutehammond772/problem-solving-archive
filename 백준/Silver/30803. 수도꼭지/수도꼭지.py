import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N = int(input())

	# 각 수도꼭지에서 내보내는 물의 양
	S = [0, *map(int, input().split())]

	# 각 수도꼭지의 토글
	T = [True] * (N + 1)

	# 초기 상태
	total = sum(S)
	print(total)

	# 각 쿼리를 수행
	Q = int(input())

	for _ in range(Q):
		A, *B = map(int, input().split())

		# 수도꼭지의 물의 양 조절
		if A == 1:
			i, X = B

			# 수도꼭지가 열려 있는 경우에만 반영
			if T[i]:
				total += X - S[i]

			S[i] = X

			print(total)

		# 수도꼭지 토글
		elif A == 2:
			i = B[0]

			if T[i]:
				total -= S[i]
			else:
				total += S[i]

			T[i] = not T[i]

			print(total)
