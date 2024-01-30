import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	count = [0] * 10
	
	for i in range(N):
		count[A[i]] += 1
	
	for num in range(9, 0, -1):
		for i in range(N // 2):
			if A[i] > num or A[(N - 1) - i] > num:
				continue
				
			for k in range(9, num, -1):
				if count[k] >= 2:
					A[i] = A[(N - 1) - i] = k
					count[k] -= 2
					break
			
			if A[i] != num and A[(N - 1) - i] == num:
				A[i] = num
				count[num] -= 1
			
			if A[i] == num and A[(N - 1) - i] != num:
				A[(N - 1) - i] = num
				count[num] -= 1
	
	if N % 2:
		mid = max(x for x in range(1, 10) if count[x])
		A[N // 2] = max(A[N // 2], mid)
	
	return A

if __name__ == '__main__':
	N = int(input())
	A = [int(ch) for ch in input()]
	
	result = solve(N, A)
	print(*result, sep="")
	