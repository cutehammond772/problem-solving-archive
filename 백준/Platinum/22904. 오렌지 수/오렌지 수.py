import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(K):
	if K % 9 not in [0, 1]:
		return [-1]
	
	sequence = deque([])
	result = []
	
	if K % 9:
		sequence.append('1')
	
	sequence.extend(['9'] * (K // 9))
	
	# 첫번째 수
	result.append("".join(sequence))
	
	# 두번째 수
	sequence.appendleft('1')
	sequence[-1] = '8'
	
	result.append("".join(sequence))
	
	# 세번째 수
	sequence.appendleft('1')
	sequence[-2] = '8'
	
	result.append("".join(sequence))
	
	return result

if __name__ == '__main__':
	K = int(input())
	print(*solve(K), sep='\n')
