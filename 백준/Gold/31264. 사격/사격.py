import sys, math
input = lambda: sys.stdin.readline().rstrip()

# Parametric Search
def solve(N, M, A, S):
	x, y = 1, int(1e5)
	
	# 표적 점수 순으로 정렬
	S.sort()
	
	# 진급 가능성 체크
	def check(k):
		score = 0
		shot = M
		
		if S[0] > k:
			return False
		
		for i in range(N):
			if not shot:
				break
			
			# 가장 큰 표적 점수
			if i == N - 1:
				score += S[i] * shot
				break
			
			# 현재 사격 실력에 따라 획득 가능한 가장 큰 표적에 도달
			if S[i + 1] <= k:
				continue
			
			least_shot = min(shot, math.ceil((S[i + 1] - k) / S[i]))
			
			score += S[i] * least_shot
			k += S[i] * least_shot
			shot -= least_shot
		
		return score >= A
	
	while x < y:
		k = (x + y) // 2
		
		if check(k):
			y = k
		else:
			x = k + 1
	
	return x

if __name__ == '__main__':
	N, M, A = map(int, input().split())
	S = [*map(int, input().split())]
	
	print(solve(N, M, A, S))
	