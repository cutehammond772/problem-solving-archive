import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(W, L, A):
	queue = deque(A)
	
	# (트럭의 무게, 다리에 들어온 시간)
	bridge = deque([])
	
	# 현재 다리의 상태
	truck, total_weight = 0, 0
	
	# 총 시간
	time = 0
	
	while queue or bridge:
		if bridge and (time - bridge[-1][1]) >= W:
			weight, _ = bridge.pop()
			
			truck -= 1
			total_weight -= weight
			
		if queue and truck < W:
			if queue[0] + total_weight <= L:
				weight = queue.popleft()
				bridge.appendleft((weight, time))
				
				truck += 1
				total_weight += weight
		
		time += 1
	
	return time
	
if __name__ == "__main__":
	N, W, L = map(int, input().split())
	A = [*map(int, input().split())]
	
	print(solve(W, L, A))
