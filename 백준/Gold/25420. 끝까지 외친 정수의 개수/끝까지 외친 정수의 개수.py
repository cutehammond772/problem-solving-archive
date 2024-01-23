import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 100001

def solve(N, K, A):
	# 두 명이 외칠 수 없는 정수
	check = [True] * (N + 1)
	
	for num in A:
		check[num] = False
	
	# 특정 상황에서 이길 수 있는지에 대한 여부
	game = [False] * (N + 1)
	
	# 정수 개수
	count = [0] * (N + 1)
	
	# N에 도달한 경우 앞으로 부를 수 있는 정수가 없으므로 생략한다.
	for off in range(N - 1, -1, -1):
		min_win, max_lose = INF, 0
		
		# 부를 수 있는 정수가 모두 True인 경우, 현재 플레이어는 진다.
		# 그러나, 하나라도 False가 존재하는 경우 현재 플레이어는 이길 수 있다.
		for x in range(off + 1, min(N, off + K) + 1):
			if not check[x]:
				continue
				
			if not game[x]:
				min_win = min(min_win, count[x] + 1)
			else:
				max_lose = max(max_lose, count[x] + 1)
		
		# 한 가지라도 이길 수 있는 경우가 존재할 때
		if min_win < INF:
			count[off] = min_win
			game[off] = True
		
		else:
			count[off] = max_lose
	
	return count[0]

if __name__ == "__main__":
	N, K = map(int, input().split())
	A = [*map(int, input().split())]
	
	print(solve(N, K, A))
