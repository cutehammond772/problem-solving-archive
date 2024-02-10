import sys
input = lambda: sys.stdin.readline().rstrip()

# 26, 26 * (1 + 26), 26 * (1 + 26 * (1 + 26)), ...
def solve(N, A):
	memo = [0, 26]
	result = 0
	
	for x in range(N - 1):
		memo.append(26 * (1 + memo[-1]))
	
	for x in range(len(A)):
		result += A[x] * memo[(N - 1) - x] + (A[x] + 1)
	
	return result

if __name__ == "__main__":
	N = int(input())
	A = [ord(ch) - ord('a') for ch in input()]
	
	print(solve(N, A))
	