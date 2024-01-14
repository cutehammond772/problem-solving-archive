import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(N, graph, degree, time):
	total = [0] * (N + 1)
	queue = deque([])
	
	for node in range(1, N + 1):
		if degree[node] == 0:
			total[node] = time[node]
			queue.append(node)
	
	while queue:
		node = queue.popleft()
		
		for next in graph[node]:
			degree[next] -= 1
			total[next] = max(total[next], total[node] + time[next])
			
			if degree[next] == 0:
				queue.append(next)
	
	return total[1:]

if __name__ == '__main__':
	N = int(input())
	
	graph = [[] for _ in range(N + 1)]
	degree = [0] * (N + 1)
	time = [0] * (N + 1)
	
	for j in range(1, N + 1):
		T, *B = map(int, input().split())
		time[j] = T
		
		for i in B:
			if i == -1:
				break
			
			graph[i].append(j)
			degree[j] += 1
	
	result = solve(N, graph, degree, time)
	print(*result, sep="\n")
	