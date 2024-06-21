import sys
input = lambda: sys.stdin.readline().rstrip()


# 2 ~ N 까지의 소수 구하기
def primes(N):
	check = [True] * (N + 1)
	
	for x in range(2, N + 1):
		if not check[x]:
			continue
		
		for k in range(x * 2, N + 1, x):
			check[k] = False
	
	return [x for x in range(2, N + 1) if check[x]]


def solve(N, A):
	result = []
	
	count = [0] * 1000001
	possible = 0
	
	checking_primes = primes(1000)
	
	for i in range(N):
		num = A[i]
		
		for x in checking_primes:
			initial = count[x]
			
			# 소인수 분해
			while not (num % x):
				num //= x
				count[x] += 1
			
			if (initial % 2) and not (count[x] % 2):
				possible -= 1
			
			elif not (initial % 2) and (count[x] % 2):
				possible += 1
		
		if num != 1:
			initial = count[num]
			count[num] += 1
			
			if (initial % 2) and not (count[num] % 2):
				possible -= 1
			
			elif not (initial % 2) and (count[num] % 2):
				possible += 1
		
		result.append("NE" if possible else "DA")
	
	return result


if __name__ == "__main__":
	N = int(input())
	A = [int(input()) for _ in range(N)]
	
	result = solve(N, A)
	print(*result, sep="\n")
