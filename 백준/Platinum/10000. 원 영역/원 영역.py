import sys
sys.setrecursionlimit(3 * (10 ** 5) + 10)
input = lambda: sys.stdin.readline().rstrip()

def solve(N, C):
	# 좌표 오름차순, 원이 큰 것부터 먼저 오도록 정렬한다.
	C.sort(key=lambda t: (t[0], -t[1]))
	result = 1

	def calculate(off):
		nonlocal result

		# 하나의 원은 최소 하나의 영역을 만든다.
		result += 1
		next = off + 1

		l, r = C[off]
		accu = 0

		while next < N:
			nl, nr = C[next]

			if r <= nl:
				break

			# 해당 원의 내부 원을 모두 고려한 후 다음 원의 인덱스를 반환한다.
			accu += nr - nl
			next = calculate(next)

		# 원 내부의 원들이 꽉 차면 (해당 원은) 총 두 개의 영역을 생성하게 된다.
		if accu == r - l:
			result += 1

		return next

	off = 0
	while off < N:
		off = calculate(off)

	return result

if __name__ == "__main__":
	N = int(input())
	circles = []

	for _ in range(N):
		xi, ri = map(int, input().split())
		circles.append((xi - ri, xi + ri))

	print(solve(N, circles))
