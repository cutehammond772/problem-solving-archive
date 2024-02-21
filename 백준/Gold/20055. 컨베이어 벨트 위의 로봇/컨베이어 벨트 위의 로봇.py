import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K, A):
	# 내구도가 0인 칸의 개수
	count = 0
	
	# 현재 단계
	phase = 0
	
	# 각 칸의 현재 위치
	queue = deque([*range(2 * N)])
	
	# 현재 로봇
	robots = deque([])
	
	while count < K:
		# 1. 회전
		phase += 1
		queue.appendleft(queue.pop())
		
		for x in range(len(robots)):
			robots[x] += 1
		
		# 2. 내리는 위치에 도달한 로봇 제거
		if robots and robots[-1] == N - 1:
			robots.pop()
		
		# 3. 이동
		for x in range(len(robots) - 1, -1, -1):
			# 뒷칸의 내구도가 0인 경우
			if A[queue[robots[x] + 1]] == 0:
				continue
			
			# 뒤에 바로 로봇이 있는 경우
			if (x < len(robots) - 1) and (robots[x] + 1 == robots[x + 1]):
				continue
			
			A[queue[robots[x] + 1]] -= 1
			count += (A[queue[robots[x] + 1]] == 0)
			robots[x] += 1
			
		# 3-1. 내리는 위치에 도달한 로봇 제거
		if robots and robots[-1] == N - 1:
			robots.pop()
		
		# 4. 새로운 로봇 놓기
		if A[queue[0]] > 0:
			robots.appendleft(0)
			
			A[queue[0]] -= 1
			count += (A[queue[0]] == 0)
	
	return phase

if __name__ == "__main__":
	N, K = map(int, input().split())
	A = [*map(int, input().split())]
	
	print(solve(N, K, A))
	