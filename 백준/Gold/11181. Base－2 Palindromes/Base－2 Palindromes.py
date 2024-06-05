import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
	X, L = 2, 1

	while N > X:
		N -= X; X *= 2; L += 1

	# 길이 홀수 여부
	odd = N <= (X // 2)
	N = N - 1 if N <= (X // 2) else (N - 1) - (X // 2)

	string = [0] * L

	for i in range(L - 1):
		string[i] = 1 if N & (1 << i) else 0

	string[-1] = 1

	if odd:
		return string[::-1] + string[1:]
	else:
		return string[::-1] + string

if __name__ == "__main__":
	N = int(input())

	result = solve(N)
	number = 0

	for x in range(len(result)):
		number |= result[x] << x

	print(number)
