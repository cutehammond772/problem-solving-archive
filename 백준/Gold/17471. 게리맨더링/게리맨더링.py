import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
INF = 1001

def valid(N, A, G):
	check = [False] * N
	area = [0, 0]
	queue = deque([])
	
	for i in range(N):
		if check[i]:
			continue
		
		area[(A >> i) & 1] += 1
		check[i] = True
		queue.append(i)
		
		while queue:
			node = queue.popleft()
			
			for next in G[node]:
				if ((A >> node) & 1) != ((A >> next) & 1):
					continue
				
				if check[next]:
					continue
				
				check[next] = True
				queue.append(next)
	
	return area[0] == area[1] == 1

def solve(N, A, G):
	result = INF
	
	for area in range(1, (1 << N) - 1):
		if not valid(N, area, G):
			continue
		
		memo = [0, 0]
		
		for x in range(N):
			memo[(area >> x) & 1] += A[x]
		
		result = min(result, abs(memo[0] - memo[1]))
	
	return result if result < INF else -1

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	G = [[] for _ in range(N)]
	
	for i in range(N):
		P, *Q = map(int, input().split())
		
		if P == 0:
			continue
		
		for j in Q:
			G[i].append(j - 1)
	
	print(solve(N, A, G))
	