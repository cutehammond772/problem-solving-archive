import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = [0, 1, 3, 6, 3, 6, 2]
REM = [[], [1], [1, 2, 4], [1, 3, 2, 6, 4, 5], [1, 4, 2], [1, 5, 4, 6, 2, 3], [1, 6]]

def solve(A, B, C, K, L):
	# A^(B^C) = 7 * a + b로 나타낼 수 있다.
	# 즉, A의 7의 나머지의 주기를 통해 b를 쉽게 구할 수 있다.
	# A = 1 : b = [1, ...] -> B^C % 1
	# A = 2 : b = [1, 2, 4, ...] -> B^C % 3
	# A = 3 : b = [1, 3, 2, 6, 4, 5, ...] -> B^C % 6
	# A = 4 : b = [1, 4, 2, ...] -> B^C % 3
	# A = 5 : b = [1, 5, 4, 6, 2, 3, ...] -> B^C % 6
	# A = 6 : b = [1, 6, ...] -> B^C % 2
	b = REM[A][pow(B, C, MOD[A])]
	
	# B^C / A = 7p + q -> "B^C = 7Ap + Aq" 이므로,
	# 7A로 나눈 나머지를 구한 후 A로 나누면 된다.
	q = pow(B, C, 7 * A) // A
	
	result = 0
	
	if (K + b) % 7 == L:
		result |= 1
	
	if (K + q) % 7 == L:
		result |= 2
	
	return result

if __name__ == '__main__':
	A, B, C = map(int, input().split())
	K, L = map(int, input().split())
	
	print(solve(A, B, C, K, L))
	