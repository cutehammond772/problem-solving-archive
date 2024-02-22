import sys
input = lambda: sys.stdin.readline().rstrip()
UNCHECKED = -1
MOD = int(1e6)

# 열의 n번째 자리에 블록을 배치
moves = [
	[(27, 2), (153, 1), (51, 2), (89, 1), (23, 3), (15, 4), (39, 3), (201, 1), (57, 1), (147, 2), (75, 2)],
	[(27, 2), (153, 1), (15, 4), (45, 1), (29, 1), (89, 1), (77, 1), (75, 2), (147, 2), (105, 1), (201, 1)],
	[(45, 1), (77, 1), (15, 4), (105, 1)]
]

def solve(N):
	memo = [[UNCHECKED] * 256 for _ in range(N * 3 + 1)]
	
	def go(idx, data):
		if idx > N * 3:
			return 0
		
		if idx == N * 3:
			return data == 0
		
		if memo[idx][data] != UNCHECKED:
			return memo[idx][data]
		
		total = 0
		
		if data & 1:
			memo[idx][data] = go(idx + 1, data >> 1)
			return memo[idx][data]
		
		for bit, move in moves[idx % 3]:
			if not (data & bit):
				total = (total + go(idx + move, (data | bit) >> move)) % MOD
		
		memo[idx][data] = total
		return memo[idx][data]
	
	return go(0, 0)

if __name__ == "__main__":
	N = int(input())
	print(solve(N))
	