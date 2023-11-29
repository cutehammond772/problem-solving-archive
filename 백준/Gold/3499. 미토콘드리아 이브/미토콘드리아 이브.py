import sys
input = lambda: sys.stdin.readline().rstrip()

class Analyzer:
	MALE, FEMALE = 0, 1

	def __init__(self):
		self.id = 1

		self.root = [0]
		self.gender = [0]
		self.alive = [0]
		self.dna = [0]

	def add_ancestor(self, gender):
		self.root.append(self.id)
		self.gender.append(gender)
		self.alive.append(True)
		self.dna.append(-1)

		self.id += 1

	def add_child(self, dadID, momID, gender):
		self.root.append(self.root[momID])
		self.gender.append(gender)
		self.alive.append(True)
		self.dna.append(-1)

		self.id += 1

	def die(self, id):
		self.alive[id] = False

	def set_dna(self, id, dna):
		self.dna[self.root[id]] = dna

	def check(self):
		# 1. 모계 조상을 먼저 확인한다.
		ancestors = set()

		for id in range(1, self.id):
			if self.alive[id]:
				ancestors.add(self.root[id])

		if len(ancestors) == 1:
			return "YES"

		# 2. 각 조상의 미토콘드리아 DNA를 확인한다.
		total_dna = set()
		unspecified = False

		for id in ancestors:
			dna = self.dna[id]

			if dna < 0:
				unspecified = True

			else:
				total_dna.add(dna)

		if len(total_dna) > 1:
			return "NO"

		if unspecified:
			return "POSSIBLY"

		return "YES"

if __name__ == '__main__':
	analyzer = Analyzer()

	# 조상 추가
	N = int(input())

	for _ in range(N):
		gender = input()
		analyzer.add_ancestor(gender)

	# 출생, 사망 정보
	M = int(input())

	for _ in range(M):
		P, *Q = input().split()

		# 사망
		if int(P) < 0:
			analyzer.die(-int(P))

		# 출생
		else:
			analyzer.add_child(int(P), int(Q[0]), Q[1])

	# DNA 정보
	K = int(input())

	for _ in range(K):
		id, dna = map(int, input().split())
		analyzer.set_dna(id, dna)

	# 결과
	print(analyzer.check())
