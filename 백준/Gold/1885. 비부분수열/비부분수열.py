import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(K, S):
	# 가능한 부분수열의 최대 길이
	result = 0
	
	# 1 ~ N이 모두 모여야 한다.
	# (1234..N)(1234..N).. 형태가 되어야 특정 길이의 "모든 부분 수열"을 구성할 수 있다.
	check = [False] * (K + 1)
	count = K
	
	for num in S:
		if not check[num]:
			check[num] = True
			count -= 1
		
		if not count:
			result += 1
			
			check = [False] * (K + 1)
			count = K
	
	return result + 1

if __name__ == "__main__":
	N, K = map(int, input().split())
	S = [int(input()) for ch in range(N)]
	
	print(solve(K, S))
	