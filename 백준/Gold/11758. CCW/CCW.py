import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	x1, y1 = map(int, input().split())
	x2, y2 = map(int, input().split())
	x3, y3 = map(int, input().split())

	ccw = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)

	if not ccw:
		print(0)
	else:
		print(ccw // abs(ccw))
