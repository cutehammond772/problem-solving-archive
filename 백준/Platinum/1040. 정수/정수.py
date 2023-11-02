import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 1e20

def analyse(N, K):
	fragment = []

	while N:
		fragment.append(N % 10)
		N //= 10

	fragment = [0] * max(0, K - len(fragment)) + fragment[::-1]
	return fragment, len(fragment)

def count(bit):
	result = 0

	while bit:
		result += bit & 1
		bit >>= 1

	return result

def convert(bit):
	return [x for x in range(10) if bit & (1 << x)]

def solve(N, K):
	memo = [INF] * (1 << 10)
	F, L = analyse(N, K)

	def min_combination(nums, check, offset):
		result = 0
		idx = K - 1

		for x in range(L - offset):
			while check[idx] and idx:
				idx -= 1

			result += nums[idx] * (10 ** x)
			check[idx] += 1

		while check[idx] and idx:
			idx -= 1

		return INF if idx or (not check[idx]) else result

	def traverse(nums, check, bit, offset, total):
		if memo[bit] <= total:
			return

		if offset >= L:
			if not check.count(0):
				memo[bit] = min(memo[bit], total)

			return

		for i in range(K):
			num = nums[i]

			if F[offset] > num:
				continue

			if F[offset] == num and not (offset == 0 and num == 0):
				check[i] += 1

				next_total = total + num * (10 ** ((L - 1) - offset))
				traverse(nums, check, bit, offset + 1, next_total)

				check[i] -= 1

			if F[offset] < num:
				comb_check = check[:]
				comb_check[i] += 1

				next_total = total + num * (10 ** ((L - 1) - offset))
				memo[bit] = min(memo[bit], next_total + min_combination(nums, comb_check, offset + 1))

	# 0 하나만 고르는 경우는 없도록 한다.
	for bit in range(2, 1 << 10):
		if not count(bit) == K:
			continue

		nums = convert(bit)
		check = [0] * K

		# Case 1. 가장 큰 자리수부터 비교
		traverse(nums, check, bit, 0, 0)

		# Case 2. 앞에 자리수를 하나 더 생성
		initial = 1 if not nums[0] else 0
		check[initial] += 1

		memo[bit] = min(memo[bit], nums[initial] * (10 ** L) + min_combination(nums, check, 0))

	return min(memo)

if __name__ == "__main__":
  N, K = map(int, input().split())
  print(solve(N, K))
