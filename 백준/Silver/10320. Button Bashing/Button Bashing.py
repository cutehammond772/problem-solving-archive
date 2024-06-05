import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

def solve(T, B):
	memo = [INF] * 3601
	queue = deque()

	memo[0] = 0
	queue.append((0, 0))

	while queue:
		count, time = queue.popleft()

		if memo[time] < count:
			continue

		for button in B:
			next_time = min(3600, max(0, time + button))
			next_count = count + 1

			if memo[next_time] <= next_count:
				continue

			memo[next_time] = next_count
			queue.append((next_count, next_time))

	result = (INF, INF)

	for time in range(T, 3601):
		if memo[time] < INF:
			result = min(result, (time, memo[time]))

	return result

if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		n, t = map(int, input().split())
		buttons = [*map(int, input().split())]

		time, count = solve(t, buttons)
		print(count, time - t)
