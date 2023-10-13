import math, random

def sign(x):
	return 1 if x > 0 else -1 if x < 0 else 0

# Floyd-Rivest algorithm
# 참고 : https://en.wikipedia.org/wiki/Floyd%E2%80%93Rivest_algorithm
def select(arr, left, right, k):
	while right > left:
		if right - left > 600:
			n = right - left + 1
			i = k - left + 1
			z = math.log(n)

			s = 0.5 * math.exp(2 * z / 3)
			sd = 0.5 * math.sqrt(z * s * (n - s) / n) * sign(i - n / 2)

			select(arr,
			       int(max(left, k - i * s / n + sd)),
			       int(min(right, k + (n - i) * s / n + sd)), k)

		t, i, j = arr[k], left, right
		arr[left], arr[k] = arr[k], arr[left]

		if arr[right] > t:
			arr[left], arr[right] = arr[right], arr[left]

		while i < j:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j -= 1

			while arr[i] < t:
				i += 1

			while arr[j] > t:
				j -= 1

		if arr[left] == t:
			arr[left], arr[j] = arr[j], arr[left]
		else:
			j += 1
			arr[right], arr[j] = arr[j], arr[right]

		if j <= k:
			left = j + 1

		if k <= j:
			right = j - 1

	return arr[k]

def kth(a, k):
	return select(a, 0, len(a) - 1, k - 1)
