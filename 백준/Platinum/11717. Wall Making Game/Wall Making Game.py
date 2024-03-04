import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(H, W, board):
	memo = [[-1] * 400 for _ in range(400)]
	
	# 단일 칸에 대해 미리 계산
	for h in range(H):
		for w in range(W):
			memo[h * W + w][h * W + w] = 1 if board[h][w] == '.' else 0
	
	def mex(sequence):
		count = [0] * (max(sequence) + 1)
		
		for num in sequence:
			count[num] += 1
		
		for x in range(len(count)):
			if not count[x]:
				return x
		
		return len(count)
		
	def game(h1, w1, h2, w2):
		p1, p2 = h1 * W + w1, h2 * W + w2
		
		# 유효하지 않은 보드인 경우
		if h1 > h2 or w1 > w2:
			return 0
		
		# 이미 계산된 경우 반환
		if memo[p1][p2] >= 0:
			return memo[p1][p2]
		
		# 스프라그-그런디
		candidate = []
		
		for h in range(h1, h2 + 1):
			for w in range(w1, w2 + 1):
				if board[h][w] == 'X':
					continue
				
				left_top = game(h1, w1, h - 1, w - 1)
				right_top = game(h1, w + 1, h - 1, w2)
				left_bottom = game(h + 1, w1, h2, w - 1)
				right_bottom = game(h + 1, w + 1, h2, w2)
				
				candidate.append(left_top ^ right_top ^ left_bottom ^ right_bottom)
		
		memo[p1][p2] = mex(candidate) if candidate else 0
		return memo[p1][p2]
	
	return game(0, 0, H - 1, W - 1)

if __name__ == '__main__':
	H, W = map(int, input().split())
	board = [input() for _ in range(H)]
	
	result = solve(H, W, board)
	print("First" if result else "Second")
	