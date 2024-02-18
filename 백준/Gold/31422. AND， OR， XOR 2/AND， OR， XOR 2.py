import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 998_244_353

# 문제 풀이
def solve(N, A):
	total = sum(A)
	AND = OR = XOR = total % MOD
	
	# 2진수의 각 자리수를 따진다.
	for x in range(32):
		bit, streak = 0, 0
		OR = (OR + (N * (N - 1) // 2) * (1 << x)) % MOD
		
		# 1. AND, OR 계산
		for i in range(N):
			next = (A[i] & (1 << x)) >> x
			
			if not streak:
				bit = next
				streak = 1
				continue
			
			if bit == next:
				streak += 1
				continue
			
			# 두 칸 이상 연속되어야 한다.
			elif streak == 1:
				bit = next
				continue
				
			c = ((streak * (streak - 1) // 2) * (1 << x)) % MOD
			
			# 연속된 1 구간
			if bit == 1:
				AND = (AND + c) % MOD
			
			# 연속된 0 구간
			elif bit == 0:
				OR = (OR - c) % MOD
			
			bit = next
			streak = 1
		
		if streak > 1:
			c = ((streak * (streak - 1) // 2) * (1 << x)) % MOD
			
			# 연속된 1 구간
			if bit == 1:
				AND = (AND + c) % MOD
			
			# 연속된 0 구간
			elif bit == 0:
				OR = (OR - c) % MOD
	
		# 2. XOR 계산
		# odd[n], even[n] : n까지의 연속된 구간 중, 1의 개수가 홀/짝인 구간
		odd, even = [0] * N, [0] * N
		
		bit = (A[0] & (1 << x)) >> x
		(odd if bit else even)[0] += 1
		
		for i in range(1, N):
			bit = (A[i] & (1 << x)) >> x
			(odd if bit else even)[i] += 1
			
			if bit:
				even[i] += odd[i - 1]
				odd[i] += even[i - 1]
			
			else:
				even[i] += even[i - 1]
				odd[i] += odd[i - 1]
			
			XOR = (XOR + (odd[i] - bit) * (1 << x)) % MOD
		
	return AND % MOD, OR % MOD, XOR % MOD

if __name__ == "__main__":
	N = int(input())
	A = [*map(int, input().split())]
	
	print(*solve(N, A))
	