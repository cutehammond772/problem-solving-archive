import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, matrix):
	result = 0
	all = 2 ** (N * M) - 1
	
	def make(offset, check, accumulation):
		nonlocal result
		
		for x in range(offset, N * M):
			if check & (1 << x) > 0:
				continue
				
			row, col = x // M, x % M
			
			# itself
			check |= 1 << x
			make(offset + 1, check, accumulation + matrix[row][col])
			
			# to right
			right = matrix[row][col]
			right_mask = 0
			
			for k in range(col + 1, M):
				next = row * M + k
				
				if check & (1 << next) > 0:
					break
					
				right = right * 10 + matrix[row][k]
				right_mask |= 1 << next
				
				make(x + 1, check | right_mask, accumulation + right)
				
			# to bottom
			bottom = matrix[row][col]
			bottom_mask = 0
			
			for k in range(row + 1, N):
				next = k * M + col
				
				if check & (1 << next) > 0:
					break
				
				bottom = bottom * 10 + matrix[k][col]
				bottom_mask |= 1 << next
				
				make(x + 1, check | bottom_mask, accumulation + bottom)
				
			break
			
		if check == all:
			result = max(result, accumulation)
	
	make(0, 0, 0)
	return result
	
if __name__ == '__main__':
	N, M = map(int, input().split())
	matrix = [[int(ch) for ch in input()] for _ in range(N)]
	
	print(solve(N, M, matrix))
	