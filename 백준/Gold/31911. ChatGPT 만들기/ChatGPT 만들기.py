import sys
input = lambda: sys.stdin.readline().rstrip()

def to_char(idx):
	if idx == 26:
		return '['

	if idx == 27:
		return ']'

	if idx == 28:
		return '-'

	return chr(ord('a') + idx)

def to_index(ch):
	if ch == '-':
		return 28

	if ch == '[':
		return 26

	if ch == ']':
		return 27

	return ord(ch) - ord('a')

def analyse(S):
	# 빈도 분석
	matrix = [[0] * 29 for _ in range(29)]
	result = [chr(0)] * 29

	for sentence in S:
		for x in range(len(sentence) - 1):
			matrix[to_index(sentence[x])][to_index(sentence[x + 1])] += 1

	for x in range(29):
		most = (0, -128)

		for y in range(29):
			most = max(most, (matrix[x][y], -ord(to_char(y))))

		result[x] = chr(-most[1])

	return result

def create_pattern(analysis):
	check = [-1] * 29
	result = []

	pointer = to_index('[')

	while True:
		# 패턴이 무한대로 존재하는 경우
		if check[pointer] >= 0:
			return len(result) - check[pointer], result

		check[pointer] = len(result)
		result.append(to_char(pointer))

		if result[-1] == ']':
			break

		pointer = to_index(analysis[pointer])

	# 패턴이 유한적인 경우
	return 0, result

def solve(K, M, S):
	result = []
	K -= 1

	analysis = analyse(S)
	size, pattern = create_pattern(analysis)
	L = len(pattern)

	# 1. [...]로 끝나는 경우
	if size == 0:
		for x in range(M):
			result.append(pattern[K + x] if K + x < L else '.')

		return result

	# 2. 패턴이 무한대인 경우
	start = L - size

	# 반복되지 않는 부분이 포함되는 경우
	if K < start:
		for x in range(K, min(K + M, start)):
			result.append(pattern[x])

		M -= (start - K)

	K = max(0, K - start)
	K %= size

	pattern = pattern[-size:]

	for x in range(M):
		result.append(pattern[(K + x) % len(pattern)])

	return result

if __name__ == "__main__":
	N, K, M = map(int, input().split())
	S = [input() for _ in range(N)]

	print(*solve(K, M, S), sep='')
