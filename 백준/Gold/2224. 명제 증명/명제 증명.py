import sys
input = lambda: sys.stdin.readline().rstrip()

# 알파벳 <=> 인덱스로 컨버팅하기 위한 전처리 과정
atoi, itoa = {}, {}
A, a = ord('A'), ord('a')

for x in range(26):
	atoi[chr(A + x)] = x
	atoi[chr(a + x)] = 26 + x

	itoa[x] = chr(A + x)
	itoa[26 + x] = chr(a + x)

if __name__ == "__main__":
	N = int(input())
	matrix = [[x == y for y in range(52)] for x in range(52)]
	result = []

	for _ in range(N):
		P, _, Q = input().split()
		matrix[atoi[P]][atoi[Q]] = True

	for k in range(52):
		for i in range(52):
			for j in range(52):
				matrix[i][j] = matrix[i][j] | (matrix[i][k] and matrix[k][j])

	for p in range(52):
		for q in range(52):
			if p == q:
				continue

			if matrix[p][q]:
				result.append(f"{itoa[p]} => {itoa[q]}")

	print(len(result))
	print(*result, sep='\n')
