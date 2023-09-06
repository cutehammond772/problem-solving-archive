import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	N = int(input())
	count, start, end = 0, -1, -1
	schedules = []

	for _ in range(N):
		x, y = map(int, input().split())
		schedules.append((x, -y))

	schedules.sort()

	for x, y in schedules:
		if end <= x:
			count += 1
			start, end = x, -y

		if -y < end:
			if start == x == -y:
				count += 1
			else:
				start, end = x, -y

	print(count)
