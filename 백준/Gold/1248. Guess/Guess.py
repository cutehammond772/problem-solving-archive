import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, matrix):
	temp = []
	result = []
	
	def check(idx, current):
		accumulation = current
		
		for start in range(idx - 1, -1, -1):
			accumulation += temp[start]
			next_sign = matrix[start][idx]
			
			if next_sign == 0 and accumulation == 0:
				continue
			
			if accumulation * next_sign <= 0:
				return False
			
		return True
	
	def make(idx):
		nonlocal result
		
		# 결과물이 이미 나온 경우 (다양한 답 중 아무거나 출력 가능)
		if result:
			return
		
		# 성립하는 결과물이 나올 경우
		if idx >= N:
			result = [*temp]
			return
		
		# 현재 위치의 숫자의 부호
		sign = matrix[idx][idx]
		
		if sign == 0:
			if check(idx, 0):
				# 부호가 0이면 무조건 0일 수밖에 없다.
				temp.append(0)
				make(idx + 1)
				temp.pop()
				
			return
		
		# [+-1, +-10]
		for current in range(1 * sign, 11 * sign, sign):
			if check(idx, current):
				temp.append(current)
				make(idx + 1)
				temp.pop()
	
	# 백트래킹을 통해 결과 도출
	make(0)
	return result

def convert(N):
	sign = {'-': -1, '+': 1, '0': 0}
	
	offset = -1
	sequence = [sign[x] for x in input()]
	matrix = [[0] * N for _ in range(N)]
	
	for row in range(N):
		for col in range(row, N):
			matrix[row][col] = sequence[offset := offset + 1]
			
	return matrix

if __name__ == '__main__':
	N = int(input())
	
	# 부호열을 N*N 행렬로 변환
	matrix = convert(N)
	
	# 결과물 반환
	sequence = solve(N, matrix)
	
	# 결과물 출력
	print(*sequence)
	