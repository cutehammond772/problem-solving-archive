import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K, S):
	sequence = []
	
	for num in S:
		while K and (sequence and sequence[-1] < num):
			sequence.pop()
			K -= 1
		
		sequence.append(num)
	
	return sequence[:(len(sequence) - K)]

if __name__ == "__main__":
	N, K = map(int, input().split())
	S = [int(ch) for ch in input()]
	
	result = solve(N, K, S)
	print(*result, sep="")
	