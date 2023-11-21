import sys
from math import *
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

def primes(N):
	check = [True] * (N + 1)

	for num in range(2, int(N ** 0.5) + 1):
		if not check[num]:
			continue

		for next in range(num * 2, N + 1, num):
			check[next] = False

	return [x for x in range(2, N + 1) if check[x]]

# N! = K^t * ... 로 나타내어질 때 i = t이다.
def solve(N, K, nums):
	def resolve(K):
		result = defaultdict(int)
		off = 0

		while K > 1 and off < len(nums):
			prime = nums[off]

			while not (K % prime):
				result[prime] += 1
				K //= prime

			off += 1

		if K > 1:
			result[K] += 1

		return result

	# 소인수 분해
	nums = resolve(K)
	result = 10 ** 18

	for num in nums:
		x = floor(log(N, num))
		count = sum(N // (num ** i) for i in range(1, x + 1))
		result = min(result, count // nums[num])

	return result

if __name__ == '__main__':
	T = int(input())
	nums = primes(int(1e6))

	for _ in range(T):
		N, K = map(int, input().split())
		print(solve(N, K, nums))
