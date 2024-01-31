import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# 오름차순으로 정렬된 [1, 2, ..., N] 배열에서
# [N-5, N-3, N-1, N, N-2, N-4, N-6, ...]와 같이 배치할 때 최대가 된다.
def solve(N, A):
	result = deque([])
	A.sort(reverse=True)
	
	for i in range(N):
		if i % 2:
			result.appendleft(A[i])
		else:
			result.append(A[i])
	
	return result

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	
	print(*solve(N, A))
	