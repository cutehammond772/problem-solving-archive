import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, C, B):
	# 무게 제한이 가장 큰 크레인부터 오도록 한다.
	C.sort(reverse=True)
	
	# 무거운 박스부터 먼저 체크한다.
	B.sort(reverse=True)
	
	if C[0] < B[0]:
		return -1
	
	count, cycle = 0, 0
	check = [False] * M
	
	while count < M:
		j = 0
		
		for i in range(N):
			while j < M:
				if C[i] < B[j] or check[j]:
					j += 1
					continue
				
				check[j] = True
				count += 1
				break
		
		cycle += 1
	
	return cycle

if __name__ == "__main__":
	N = int(input())
	C = [*map(int, input().split())]
	
	M = int(input())
	B = [*map(int, input().split())]
	
	print(solve(N, M, C, B))
