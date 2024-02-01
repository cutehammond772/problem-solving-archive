import sys
from heapq import heappush, heappop
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

class ProblemRecommendSystem:
	def __init__(self):
		# 특정 문제의 정보
		self.problem = defaultdict(int)
		
		# 문제 힙
		self.easy, self.hard = [], []
		
		# 문제 추가 순서를 ID로 표현
		self.id = defaultdict(int)
		self.current_id = 1
	
	def add(self, P, L):
		self.problem[P] = L
		self.id[P] = self.current_id
		
		heappush(self.easy, (L, P, self.current_id))
		heappush(self.hard, (-L, -P, self.current_id))
		
		self.current_id += 1
	
	def recommend(self, x):
		# 가장 쉬운 문제
		if x == -1:
			while self.easy:
				L, P, problem_id = self.easy[0]
				
				if self.id[P] != problem_id:
					heappop(self.easy)
					continue
				
				return P
		
		# 가장 어려운 문제
		if x == 1:
			while self.hard:
				L, P, problem_id = self.hard[0]
				L, P = -L, -P
				
				if self.id[P] != problem_id:
					heappop(self.hard)
					continue
				
				return P
		
		return None
	
	def solved(self, P):
		self.id[P] = 0

if __name__ == "__main__":
	prs = ProblemRecommendSystem()
	
	# 1. 문제 추가
	N = int(input())
	
	for _ in range(N):
		P, L = map(int, input().split())
		prs.add(P, L)
	
	# 2. 쿼리 수행
	M = int(input())
	
	for _ in range(M):
		command, *args = input().split()
		
		if command == "add":
			P, L = map(int, args)
			prs.add(P, L)
		
		elif command == "recommend":
			x = int(args[0])
			print(prs.recommend(x))
		
		elif command == "solved":
			P = int(args[0])
			prs.solved(P)
	