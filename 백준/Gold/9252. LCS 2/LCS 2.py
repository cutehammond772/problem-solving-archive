import sys
input = lambda: sys.stdin.readline().rstrip()

def lcs(P, Q):
	LP, LQ = len(P), len(Q)
	
	# (size, (current_index), (previous index))
	memo = [[(0, (p, q), (p, q)) for q in range(LQ + 1)] for p in range(LP + 1)]
	
	for p in range(1, LP + 1):
		for q in range(1, LQ + 1):
			memo[p][q] = max(memo[p - 1][q], memo[p][q - 1], memo[p - 1][q - 1])
			
			if P[p - 1] == Q[q - 1]:
				prev_size, prev_index, _ = memo[p - 1][q - 1]
				memo[p][q] = max(memo[p][q], (prev_size + 1, (p, q), prev_index))
	
	size, curr_idx, prev_idx = memo[LP][LQ]
	sequence = []
	
	for _ in range(size):
		sequence.append(P[curr_idx[0] - 1])
		curr_idx, prev_idx = memo[prev_idx[0]][prev_idx[1]][1:]
	
	return "".join(sequence[::-1])

if __name__ == "__main__":
	P, Q = input(), input()
	result = lcs(P, Q)
	
	print(len(result))
	
	if result:
		print(result)
	