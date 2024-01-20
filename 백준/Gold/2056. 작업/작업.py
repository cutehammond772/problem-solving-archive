import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(N, times, tasks, dependencies):
	# (task, total time)
	queue = deque([task for task in range(1, N + 1) if dependencies[task] == 0])
	
	# 작업하기 전에 필요한 최소 시간
	collapsed = [0] * (N + 1)
	result = 0
	
	while queue:
		task = queue.popleft()
		result = max(result, collapsed[task] + times[task])
		
		for next in tasks[task]:
			dependencies[next] -= 1
			collapsed[next] = max(collapsed[next], collapsed[task] + times[task])
			
			if dependencies[next] == 0:
				queue.append(next)
	
	return result

if __name__ == '__main__':
	N = int(input())
	
	times = [0] * (N + 1)
	tasks = [[] for _ in range(N + 1)]
	dependencies = [0] * (N + 1)
	
	for task in range(1, N + 1):
		a, b, *T = map(int, input().split())
		
		times[task] = a
		
		for prev in T:
			tasks[prev].append(task)
			dependencies[task] += 1
	
	print(solve(N, times, tasks, dependencies))
	