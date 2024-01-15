import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	current = [0] * 21
	current[A[0]] = 1
	
	for x in range(1, N - 1):
		num = A[x]
		next = [0] * 21
		
		for total in range(21):
			# 기존 식에 더하는 경우
			if total + num <= 20:
				next[total + num] += current[total]
			
			# 기존 식에 빼는 경우
			if total - num >= 0:
				next[total - num] += current[total]
		
		current = next
	
	return current[A[-1]]

if __name__ == '__main__':
	N = int(input())
	A = [*map(int, input().split())]
	
	print(solve(N, A))
	