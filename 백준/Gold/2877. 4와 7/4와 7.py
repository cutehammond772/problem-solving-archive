import sys
input = lambda: sys.stdin.readline().rstrip()

def first(K):
	for x in range(2, 32):
		if K <= (2 ** x) - 2:
			offset, area = 2 ** (x - 1) - 2, 2 ** (x - 2)

			if offset < K <= offset + area:
				return '4', K - area

			if offset + area < K <= offset + (area * 2):
				return '7', K - (area * 2)

if __name__ == "__main__":
	K = int(input())
	result = ''

	# 1, 2, 11, 12, 21, 22, 111, 112, 121, 122, 211
	# [2], [4], [8], [16], ...

	while K:
		num, last = first(K)

		result += num
		K = last

	print(result)
