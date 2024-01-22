import sys
input = lambda: sys.stdin.readline().rstrip()

# upper bound
def find(S, t):
	x, y = 0, len(S) - 1
	
	while x < y:
		mid = (x + y) // 2
		
		if S[mid] > t:
			y = mid
		else:
			x = mid + 1
			
	return x

# column 번호를 기준으로 LIS를 구하되, 일직선으로 이동 시 같은 번호가 나열되므로
# upper bound를 사용해야 한다.
def solve(A):
	A = [t[1] for t in sorted(A)]
	S = []
	
	for t in A:
		if not S or S[-1] < t:
			S.append(t)
			continue
		
		S[find(S, t)] = t
		
	return len(S)

if __name__ == '__main__':
	N, M = map(int, input().split())
	T = int(input())
	A = []
	
	for _ in range(T):
		r, c = map(int, input().split())
		
		# 가톨릭대 밖에 고양이가 존재할 경우 접근할 수 없다.
		if r > N or c > M:
			continue
		
		A.append((r, c))
	
	print(solve(A))
	