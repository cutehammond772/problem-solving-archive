import sys
input = lambda: sys.stdin.readline().rstrip()

def change(P, cmd):
	A, B = [], []

	for x in range(8):
		if (1 << x) & cmd:
			A.append(x)

	# 유효하지 않은 명령
	if len(A) != 2:
		return

	i, j = A

	for x in range(8):
		if P[x] == i or P[x] == j:
			B.append(x)

	k, l = B
	
	P[k], P[l] = P[l], P[k]

def solve(A, K):
	# 각 점에 존재하는 키
	P = [*range(8)]

	# 키 위치 바꾸기
	for cmd in A:
		change(P, cmd)

	# K의 위치 찾기
	for t in range(8):
		if P[t] == K:
			return t

	return -1

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	K = int(input())

	print(solve(A, K))
