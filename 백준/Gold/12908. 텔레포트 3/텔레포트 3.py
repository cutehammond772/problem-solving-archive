import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 10

def solve(xs, ys, xe, ye, tps):
	result = INF
	total = []
	checked = [False] * len(tps)

	def dist(d1, d2):
		return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])

	def calculate():
		if len(total) == 0:
			return dist((xs, ys), (xe, ye))

		accumulation = 10 * len(total)

		# 중간 지점
		for x in range(1, len(total)):
			d1, d2 = total[x - 1][1], total[x][0]
			accumulation += dist(d1, d2)

		# 시작 지점
		accumulation += dist((xs, ys), total[0][0])

		# 도착 지점
		accumulation += dist(total[-1][1], (xe, ye))

		return accumulation

	def select():
		nonlocal result

		# 텔레포트가 0개 ~ 3개 추가된 상황에서 시간을 계산한다.
		result = min(result, calculate())

		for i in range(len(tps)):
			if checked[i]:
				continue

			t1, t2 = tps[i]
			checked[i] = True

			# 텔레포트는 양방향이므로 둘 다 고려한다.
			total.append((t1, t2))
			select()
			total.pop()

			total.append((t2, t1))
			select()
			total.pop()

			checked[i] = False

	select()
	return result

if __name__ == "__main__":
	xs, ys = map(int, input().split())
	xe, ye = map(int, input().split())

	tps = []
	for _ in range(3):
		x1, y1, x2, y2 = map(int, input().split())
		tps.append(((x1, y1), (x2, y2)))

	print(solve(xs, ys, xe, ye, tps))
