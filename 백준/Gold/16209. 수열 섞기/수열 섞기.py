import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def create(nums):
	result = deque([])
	
	for num in nums:
		if len(result) % 2:
			result.appendleft(num)
		else:
			result.append(num)
	
	return result

def solve(A):
	P, N = [], []
	
	for num in A:
		(P if num >= 0 else N).append(num)
	
	P.sort(reverse=True)
	N.sort()
	
	positives, negatives = create(P), create(N)
	
	if len(positives) % 2 == 0:
		positives.reverse()
	
	if len(negatives) % 2 == 1:
		negatives.reverse()
	
	return positives + negatives

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	
	print(*solve(A))
	