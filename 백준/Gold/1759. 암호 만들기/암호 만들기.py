import sys
input = lambda: sys.stdin.readline().rstrip()
consonants = { 'a', 'e', 'i', 'o', 'u' }

def check_vowel(ch):
	if ch not in consonants:
		return 1

	return 0

def solve(L, C, alphabets):
	result = []
	temp = []

	def make(offset, vowels, consonants):
		if vowels + consonants >= L:
			if vowels >= 2 and consonants >= 1:
				result.append(tuple(temp))

			return

		for idx in range(offset, C):
			alphabet = alphabets[idx]

			temp.append(alphabet)
			make(
				idx + 1,
			  vowels + check_vowel(alphabet),
			  consonants + (1 - check_vowel(alphabet))
			)
			temp.pop()

	make(0, 0, 0)
	return result

if __name__ == '__main__':
	L, C = map(int, input().split())
	alphabets = [*sorted(input().split())]

	for combination in solve(L, C, alphabets):
		print(*combination, sep='')