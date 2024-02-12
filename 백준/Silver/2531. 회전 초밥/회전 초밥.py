import sys
input = lambda: sys.stdin.readline().rstrip()

# 아이디어 : 뒤에 K - 1개만큼 앞부분을 추가하여 원형 배열의 모든 가짓수를 판단할 수 있다.
def solve(D, K, C, S):
	result, current = 0, 0
	
	A = S + S[:(K - 1)]
	count = [0] * (D + 1)
	
	# 쿠폰 반영
	count[C] += 1
	current += 1
	
	for x in range(len(A)):
		# 1. 다음 차례의 초밥을 가짓수에 반영
		if not count[A[x]]:
			current += 1
			
		count[A[x]] += 1
		
		# K개가 모두 채워질 때까지 기다리기
		if x < K - 1:
			continue
		
		# 딱 K개가 채워진 경우
		if x == K - 1:
			result = max(result, current)
			continue
		
		# 2. 가장 앞의 초밥을 가짓수에서 제거
		count[A[x - K]] -= 1
		
		if not count[A[x - K]]:
			current -= 1
		
		result = max(result, current)
	
	return result

if __name__ == "__main__":
	N, D, K, C = map(int, input().split())
	S = [int(input()) for _ in range(N)]
	
	print(solve(D, K, C, S))
	