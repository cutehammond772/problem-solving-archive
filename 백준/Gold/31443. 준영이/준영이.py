import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = int(1e9 + 7)

# 3 * 1 조각을 우선 만들면 된다.
# 남는 경우 맞아떨어질 때까지 2 * 1 조각으로 바꾼다.
def solve(N, M):
	size = N * M
	
	if size < 4:
		return size
	
	if size % 3 == 0:
		return pow(3, size // 3, MOD)
	
	if size % 3 == 1:
		return (pow(3, (size // 3) - 1, MOD) * 4) % MOD
	
	return (pow(3, size // 3, MOD) * 2) % MOD

if __name__ == '__main__':
	N, M = map(int, input().split())
	print(solve(N, M))
	