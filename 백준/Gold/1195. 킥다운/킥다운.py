import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(A, B):
	# B가 더 짧은 기어 파트가 되도록 한다.
	if len(A) < len(B):
		A, B = B, A

	LA, LB = len(A), len(B)
	result = LA + LB

	# A를 기준으로 양 옆에 B - 1만큼 빈 칸을 만든다.
	board = [1] * (LA + 2 * (LB - 1))
	board[(LB - 1):(LB - 1 + LA)] = A

	for off in range(len(board) - (LB - 1)):
		possible = True

		for x in range(LB):
			if board[off + x] == B[x] == 2:
				possible = False
				break

		if possible:
			result = min(result, max(0, (LB - 1) - off) + max(0, off - (LA - 1)) + LA)

	return result

if __name__ == "__main__":
	A, B = [int(x) for x in input()], [int(x) for x in input()]
	print(solve(A, B))
