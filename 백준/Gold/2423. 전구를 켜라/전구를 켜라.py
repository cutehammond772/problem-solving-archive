import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

def vertices(r, c, M):
	left_top = r * (M + 1) + c
	right_top = r * (M + 1) + (c + 1)
	left_bottom = (r + 1) * (M + 1) + c
	right_bottom = (r + 1) * (M + 1) + (c + 1)
	
	return left_top, right_bottom, left_bottom, right_top

def solve(N, M, G):
	memo = [INF] * ((N + 1) * (M + 1))
	
	# (node, dist)
	queue = deque([(0, 0)])
	memo[0] = 0
	
	# 0-1 BFS
	while queue:
		node, dist = queue.popleft()
		
		if memo[node] < dist:
			continue
		
		for next, cost in G[node]:
			if memo[next] <= dist + cost:
				continue
			
			memo[next] = dist + cost
	
			if cost == 0:
				queue.appendleft((next, dist + cost))
			
			else:
				queue.append((next, dist + cost))
	
	result = memo[-1]
	return result if result < INF else "NO SOLUTION"

if __name__ == "__main__":
	N, M = map(int, input().split())
	
	# 각 회로의 꼭짓점을 정점으로 한다.
	G = [[] for _ in range((N + 1) * (M + 1))]
	
	# 그래프를 형성한다.
	for row in range(N):
		data = input()
		
		for col in range(M):
			v1, v2, v3, v4 = vertices(row, col, M)
			
			if data[col] == '/':
				G[v3].append((v4, 0))
				G[v4].append((v3, 0))
				
				# 90도 회전한 경우
				G[v1].append((v2, 1))
				G[v2].append((v1, 1))
			
			if data[col] == '\\':
				G[v1].append((v2, 0))
				G[v2].append((v1, 0))
				
				# 90도 회전한 경우
				G[v3].append((v4, 1))
				G[v4].append((v3, 1))
	
	print(solve(N, M, G))
