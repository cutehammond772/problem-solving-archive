import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
	check = [False] * N
	target = 0
	
	for x in range(N):
		if A[x] != (x + 1):
			check[x] = True
			target = max(target, x + 1)
	
	# 모두 착신 전환이 되어있지 않으면, 한 칸씩 밀면 된다.
	if not target:
		return N, [*A[1:], A[0]]
	
	count = 0
	
	for x in range(N):
		if not check[x]:
			A[x] = target
			count += 1
	
	return count, A
	

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	
	count, sequence = solve(N, A)
	
	print(count)
	print(*sequence)
	