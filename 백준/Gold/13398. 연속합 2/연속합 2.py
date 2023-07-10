import sys
input = lambda: sys.stdin.readline().rstrip()

MAX = 10 ** 9

def solve(N, seq):
	result, current = -MAX, 0
	default = [0]
	
	for x in range(N):
		# 수를 제외하지 않는 기존 연속합
		default.append(max(seq[x], default[-1] + seq[x]))
		
		# 수를 제외하는 연속합
		current = max(seq[x], current + seq[x])
		
		if seq[x] < 0:
			current = max(current, default[x + 1] - seq[x])
		
		# 항상 최대값으로 유지
		result = max(result, current)
		
	# 음수로만 이루어졌을 때
	seq_max = max(seq)
	
	if seq_max < 0:
		return seq_max
	
	return result
	
if __name__ == '__main__':
	N = int(input())
	sequence = [*map(int, input().split())]
	
	print(solve(N, sequence))
		