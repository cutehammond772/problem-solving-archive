import sys, math
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# 구사과와 큐브러버가 고른 문자가 서로 번갈아 가며 적힌다.
def solve(P, Q):
	# P와 Q의 길이가 같다고 가정한다.
	N = len(P)
	
	# P : 구사과, Q : 큐브러버
	P = deque([*sorted(P)][:math.ceil(N / 2)])
	Q = deque([*sorted(Q, reverse=True)][:math.floor(N / 2)])
	
	# 맨 왼쪽부터, 맨 오른쪽부터
	left, right = [], []
	
	for x in range(N):
		if len(P) + len(Q) == 1:
			left.append((Q if x % 2 else P).pop())
			continue
		
		px, qx = P[0], Q[0]
		
		if px < qx:
			left.append((Q if x % 2 else P).popleft())
		else:
			right.append((Q if x % 2 else P).pop())
		
	return left + right[::-1]

if __name__ == "__main__":
	P, Q = input(), input()
	result = solve(P, Q)
	
	print(*result, sep="")
