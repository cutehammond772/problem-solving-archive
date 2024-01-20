import sys
input = lambda: sys.stdin.readline().rstrip()

def create(N):
	memo = [1, 1, 2, 4]
	
	for k in range(4, N + 1):
		memo.append(sum(memo[-4:]))
	
	return memo

if __name__ == '__main__':
	T = int(input())
	koong = create(67)
	
	for _ in range(T):
		N = int(input())
		print(koong[N])
	