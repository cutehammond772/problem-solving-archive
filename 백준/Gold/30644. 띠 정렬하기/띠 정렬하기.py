import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N = int(input())
	A = [*map(int, input().split())]

	# (ai, i)
	Q = [(A[i], i) for i in range(N)]
	Q.sort()

	# 인덱스의 연속성을 따진다.
	result = 0

	for x in range(1, N):
		if abs(Q[x - 1][1] - Q[x][1]) != 1:
			result += 1

	print(result)