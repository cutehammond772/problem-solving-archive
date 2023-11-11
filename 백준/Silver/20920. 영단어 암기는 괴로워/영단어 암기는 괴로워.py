import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N, M = map(int, input().split())

  frequencies = defaultdict(int)
  words = set()

  for _ in range(N):
    word = input()

    if len(word) < M:
      continue

    frequencies[word] += 1
    words.add(word)

  words = [*words]

  # 3순위. 알파벳 사전순으로 배치
  words.sort()

  # 2순위. 단어 길이 내림차순으로 배치
  words.sort(key=lambda x: -len(x))

  # 1순위. 빈도 내림차순으로 배치
  words.sort(key=lambda x: -frequencies[x])

  print(*words, sep='\n')
