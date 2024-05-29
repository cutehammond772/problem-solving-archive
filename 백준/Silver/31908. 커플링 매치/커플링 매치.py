import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
	N = int(input())
	mappings = defaultdict(list)
	result = []

	for _ in range(N):
		p, s = input().split()

		# 반지를 착용하고 있지 않은 경우
		if s == '-':
			continue

		mappings[s].append(p)

	for ring in mappings:
		if len(mappings[ring]) == 2:
			result.append(mappings[ring])

	print(len(result))

	for couple in result:
		print(*couple)
