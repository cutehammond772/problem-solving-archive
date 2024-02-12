import sys
input = lambda: sys.stdin.readline().rstrip()

# 키가 작은 사람부터, 왼쪽에 (키가 더 큰 사람들의) 자리를 만들어 주면 된다.
def solve(N, A):
	result = [0] * N
	
	for x in range(N):
		count = 0
		
		for k in range(N):
			if count == A[x] and (not result[k]):
				result[k] = 1 + x
				break
				
			count += (not result[k]) or (result[k] > 1 + x)
		
	return result

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	
	print(*solve(N, A))
