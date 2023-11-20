import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N = int(input())
	queue = deque([(0, N)])
	discover = set()

	result = -1

	while queue:
		count, num = queue.popleft()

		if num == 1:
			result = count
			break

		if (num - 1) >= 1 and (num - 1 not in discover):
			discover.add(num - 1)
			queue.append((count + 1, num - 1))

		if num % 2 == 0 and (num // 2) >= 1 and (num // 2 not in discover):
			discover.add(num // 2)
			queue.append((count + 1, num // 2))

		if num % 3 == 0 and (num // 3) >= 1 and (num // 3 not in discover):
			discover.add(num // 3)
			queue.append((count + 1, num // 3))

	print(result)
