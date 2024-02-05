import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(L, A):
	result, status = 0, 0
	A.sort(key=lambda x: -5 * x[0])
	
	for Ki, Ti in A:
		status += Ki * Ti
		
		if status > L:
			result += status - L
			status = L
		
		result += Ti
		status -= 5 * Ki
	
	return result

if __name__ == "__main__":
	N, L = map(int, input().split())
	A = []
	
	# 1. 광기를 남기지 않고 다 풀 수 있는 문제의 총 누적 시간이다.
	result = 0
	
	for _ in range(N):
		Ki, Ti = map(int, input().split())
		
		if Ti <= 5:
			result += Ti
			continue
			
		A.append((Ki, Ti))
	
	# 2. 광기가 남는 문제에 대해 누적 시간을 구한다.
	result += solve(L, A)
	print(result)
	