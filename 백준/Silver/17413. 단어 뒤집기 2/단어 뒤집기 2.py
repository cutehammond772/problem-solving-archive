import sys
input = lambda: sys.stdin.readline().rstrip()

def reverse(S, start, end):
  for x in range((end - start + 1) // 2):
    S[start + x], S[end - x] = S[end - x], S[start + x]

if __name__ == '__main__':
  S = [x for x in input()]

  # 뒤집을 단어의 범위
  start, end = 0, 0

  # 태그 여부
  tag = False

  for index in range(len(S)):
    ch = S[index]

    # 태그 진입
    if ch == '<':
      reverse(S, start, end)
      tag = True

    # 단어 범위 완성 & 태그 내에 있지 않을 때
    if ch == ' ' and not tag:
      reverse(S, start, end)
      start = index + 1

    # 태그 탈출
    if ch == '>':
      start = index + 1
      tag = False

    if not tag:
      end = index

  if end == len(S) - 1:
    reverse(S, start, end)

  print(*S, sep='')
