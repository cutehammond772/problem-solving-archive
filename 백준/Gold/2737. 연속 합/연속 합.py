import sys
input = lambda: sys.stdin.readline().rstrip()

def consecutive_sums(N):
	# result[a] = sum(0...(a - 1))
	result = [0, 0]

	while result[-1] <= N:
		result.append(result[-1] + (len(result) - 1))

	return result

def solve(N, S):
	a = 2
	result = 0

	while N > S[a]:
		result += not (N - S[a]) % a
		a += 1

	return result

if __name__ == '__main__':
	T = int(input())
	S = consecutive_sums(1 << 31)

	for _ in range(T):
		N = int(input())
		print(solve(N, S))
