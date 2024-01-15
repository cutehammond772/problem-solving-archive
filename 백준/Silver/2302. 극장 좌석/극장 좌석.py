import sys
input = lambda: sys.stdin.readline().rstrip()

def fibonacci(N):
	memo = [0] * (N + 1)
	memo[0] = memo[1] = 1
	
	for i in range(2, N + 1):
		memo[i] = memo[i - 2] + memo[i - 1]
	
	return memo

if __name__ == '__main__':
	N = int(input())
	M = int(input())
	
	A = [0]
	
	for _ in range(M):
		num = int(input())
		A.append(num)
		
	A.append(N + 1)
	
	# 피보나치 수
	fibo = fibonacci(40)
	result = 1
	
	for x in range(1, M + 2):
		result *= fibo[A[x] - A[x - 1] - 1]
	
	print(result)
	