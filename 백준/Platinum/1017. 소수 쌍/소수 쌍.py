import sys
input = lambda: sys.stdin.readline().rstrip()
NOT_MATCHED = -1

# 소수 Check를 위한 배열을 생성한다.
def create(N):
	check = [True] * (N + 1)
	check[0] = check[1] = False
	
	for num in range(2, int(N ** 0.5) + 1):
		if not check[num]:
			continue
		
		for next in range(num * 2, N + 1, num):
			check[next] = False
	
	return check

# 홀수와 짝수 간 매칭을 수행한다.
def solve(A):
	primes = create(2000)
	P, Q = [], []
	
	for num in A:
		(P if num % 2 else Q).append(num)
	
	# 모두 쌍을 이루어야 하므로 홀수와 짝수의 개수가 같아야 한다.
	if len(P) != len(Q):
		return [-1]
	
	# 편리를 위해 첫번째 수가 포함된 그룹을 P 그룹으로 설정한다.
	if A[0] % 2 == 0:
		P, Q = Q, P
	
	LP, LQ = len(P), len(Q)
	adj = [[] for _ in range(LP)]
	
	for p in range(LP):
		for q in range(LQ):
			if primes[P[p] + Q[q]]:
				adj[p].append(q)
	
	# 첫번째 수와 이미 매칭된 q는 없는 존재 취급한다.
	def match(GP, GQ, visited, p, matched_q):
		visited[p] = True
		
		for q in adj[p]:
			if q == matched_q:
				continue
				
			if GQ[q] == NOT_MATCHED or (not visited[GQ[q]] and match(GP, GQ, visited, GQ[q], matched_q)):
				GP[p], GQ[q] = q, p
				
				return True
		
		return False
	
	# 첫번째 수와 짝지을 수 있는 수
	possible = [False] * LQ
	
	# 첫번째 수와 Q 그룹의 수를 하나씩 매칭해 놓고 각각 이분 매칭을 수행한다.
	# 이때, 모두 매칭이 된 경우 첫번째 수와 매칭된 수를 확인한다.
	for q in adj[0]:
		GP, GQ = [NOT_MATCHED] * LP, [NOT_MATCHED] * LQ
		
		GP[0], GQ[q] = q, 0
		matches = 1
		
		for p in range(1, LP):
			if GP[p] != NOT_MATCHED:
				continue
			
			visited = [False] * LP
			matches += match(GP, GQ, visited, p, q)
		
		if matches == LP:
			possible[GP[0]] = True
	
	result = [Q[x] for x in range(LQ) if possible[x]]
	
	if not result:
		return [-1]
	
	return sorted(result)
		
if __name__ == '__main__':
	N = int(input())
	A = [*map(int, input().split())]
	
	print(*solve(A))
	