import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
mapping = {'K': 1, 'S': 2, 'A': 0}

def solve(N, X):
	# 시행 횟수
	count = 0
	queue = deque(X)
	
	# 문자열의 인덱스
	index = 1
	
	while queue:
		ch = queue.popleft()
		
		if mapping[ch] == index % 3:
			index += 1
			continue
		
		count += 1
	
	return count + abs((N + 1) - index)

# 왼쪽에 패딩을 최대 두 개까지 추가할 수 있다.
if __name__ == '__main__':
	X = input()
	S = [X, "K" + X, "KS" + X]
	
	result = min(x + solve(len(X), S[x]) for x in range(3))
	print(result)
	