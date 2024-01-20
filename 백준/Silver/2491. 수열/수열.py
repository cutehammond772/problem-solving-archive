import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	increment, decrement = 1, 1
	increment_temp, decrement_temp = 1, 1
	
	for i in range(1, N):
		if A[i - 1] == A[i]:
			increment_temp += 1
			decrement_temp += 1
		
		elif A[i - 1] < A[i]:
			increment_temp += 1
			decrement_temp = 1
		
		elif A[i - 1] > A[i]:
			increment_temp = 1
			decrement_temp += 1
		
		increment = max(increment, increment_temp)
		decrement = max(decrement, decrement_temp)
	
	return max(increment, decrement)

if __name__ == '__main__':
	N = int(input())
	A = [*map(int, input().split())]
	
	print(solve(N, A))
	