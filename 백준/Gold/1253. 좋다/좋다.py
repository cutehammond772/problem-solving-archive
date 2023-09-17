import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]

	# 수를 정렬한다.
	# "다른 위치면 값이 같아도 다른 수"는 동일하게 적용된다.
	A.sort()
	result = 0

	for k in range(N):
		# 양쪽 끝 원소부터 시작한다.
		x, y = 0, N - 1

		while x < y:
			if k == x:
				x += 1
				continue

			if k == y:
				y -= 1
				continue

			num = A[x] + A[y]

			if num == A[k]:
				result += 1
				break

			if num > A[k]:
				y -= 1

			if num < A[k]:
				x += 1

	print(result)
	