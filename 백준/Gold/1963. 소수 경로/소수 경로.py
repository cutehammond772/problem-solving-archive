import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

prime = [True] * 10000
INF = int(1e10)

def init():
	for x in range(2, 100):
		if not prime[x]:
			continue
		
		for y in range(x * 2, 10000, x):
			prime[y] = False

def solve(A, B):
	check = [INF] * 10000
	queue = deque([])
	
	check[A] = 0
	queue.append(A)
	
	while queue:
		raw_number = queue.popleft()
		
		# BFS 특성상 가장 먼저 도달한 경우가 최소 회수이다.
		if raw_number == B:
			break
		
		current_number = [*str(raw_number)]
		
		for x in range(4):
			for digit in range(10):
				# 가장 앞 자리수에 0은 허용되지 않는다.
				if (x | digit) == 0:
					continue
				
				current_digit = current_number[x]
				current_number[x] = str(digit)
				
				next_number = int("".join(current_number))
				current_number[x] = current_digit
				
				if not prime[next_number]:
					continue
				
				if check[next_number] <= check[raw_number] + 1:
					continue
				
				check[next_number] = check[raw_number] + 1
				queue.append(next_number)
	
	return check[B]

if __name__ == "__main__":
	T = int(input())
	init()
	
	for _ in range(T):
		A, B = map(int, input().split())
		print(solve(A, B))
	