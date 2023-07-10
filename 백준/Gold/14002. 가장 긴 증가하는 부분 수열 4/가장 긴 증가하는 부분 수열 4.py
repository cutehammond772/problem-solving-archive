import sys
input = lambda: sys.stdin.readline().rstrip()

def lower_bound(A, K):
	x, y = 0, len(A)
	
	while x < y:
		mid = (x + y) // 2
		
		if A[mid] >= K:
			y = mid
		else:
			x = mid + 1
			
	return x

def solve(N, sequence):
	temp, logs = [], []
	
	for x in range(N):
		next = sequence[x]
		
		if not temp or temp[-1] < next:
			logs.append((len(temp), next))
			temp.append(next)
		else:
			idx = lower_bound(temp, next)
			logs.append((idx, next))
			temp[idx] = next
			
	L = len(temp)
	offset = L - 1
	result = [0] * L
	
	for k in range(N - 1, -1, -1):
		idx, num = logs[k]
		
		if offset == idx:
			result[offset] = num
			offset -= 1
			
	return L, result
	
if __name__ == '__main__':
	N = int(input())
	sequence = [*map(int, input().split())]
	size, result = solve(N, sequence)
	
	print(size)
	print(*result)
	