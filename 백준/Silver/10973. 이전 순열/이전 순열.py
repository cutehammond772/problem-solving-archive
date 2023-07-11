import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, seq):
	start = -1
	check = [True] * (N + 1)
	
	for idx in range(N - 2, -1, -1):
		check[seq[idx + 1]] = False
		
		if seq[idx] > seq[idx + 1]:
			start = idx
			break
	
	if start == -1:
		return [-1]
	
	result = seq[:start]
	check[seq[start]] = False
	
	for next in range(seq[start] - 1, 0, -1):
		if not check[next]:
			result.append(next)
			check[next] = True
			break
	
	for next in range(N, -1, -1):
		if not check[next]:
			result.append(next)
			
	return result
	
if __name__ == '__main__':
	N = int(input())
	sequence = [*map(int, input().split())]
	
	previous = solve(N, sequence)
	print(*previous)
	