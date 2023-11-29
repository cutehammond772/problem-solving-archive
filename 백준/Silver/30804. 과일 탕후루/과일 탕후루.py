import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N = int(input())
	S = [*map(int, input().split())]
	result = offset = species = 0

	# 현재 구역의 과일의 가짓수
	count = [0] * 10

	for end in range(N):
		fruit = S[end]

		# 과일 집계
		if count[fruit] == 0:
			species += 1

		count[fruit] += 1

		# 과일 가짓수 줄이기
		while species > 2:
			first_fruit = S[offset]
			count[first_fruit] -= 1

			if count[first_fruit] == 0:
				species -= 1

			offset += 1

		result = max(result, end - offset + 1)

	print(result)
