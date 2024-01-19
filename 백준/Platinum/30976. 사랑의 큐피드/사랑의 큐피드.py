import sys
sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline().rstrip()
NOT_MATCHED = -1

def solve(N, M, G, B, L, U):
	graph = [[] for _ in range(N)]
	
	# 서로 선호 기준에 맞는 쌍을 추가
	for girl in range(N):
		for boy in range(M):
			if L[girl] > B[boy] and U[boy] < G[girl]:
				graph[girl].append(boy)
	
	GG, GB = [NOT_MATCHED] * N, [NOT_MATCHED] * M
	matches = 0
	
	def match(check, girl):
		check[girl] = True
		
		for boy in graph[girl]:
			if GB[boy] == NOT_MATCHED or (not check[GB[boy]] and match(check, GB[boy])):
				GG[girl], GB[boy] = boy, girl
				return True
		
		return False
	
	for girl in range(N):
		if GG[girl] != NOT_MATCHED:
			continue
		
		check = [False] * N
		matches += match(check, girl)
	
	return matches

if __name__ == '__main__':
	N, M = map(int, input().split())
	
	# 여학생의 키
	G = [*map(int, input().split())]
	
	# 남학생의 키
	B = [*map(int, input().split())]
	
	# 여학생의 선호 기준 (작아야 함)
	L = [*map(int, input().split())]
	
	# 남학생의 선호 기준 (커야 함)
	U = [*map(int, input().split())]
	
	print(solve(N, M, G, B, L, U))
	