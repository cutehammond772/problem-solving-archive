import sys, re
input = lambda: sys.stdin.readline().rstrip()
pattern = re.compile(r"</?[A-Za-z0-9-]+>")
CHAR, SKIP = -1, -2

def diff(prev, curr):
  offset = min(len(prev), len(curr))

  for x in range(min(len(prev), len(curr))):
    if prev[x] != curr[x]:
      offset = x
      break

  added = curr[offset:]
  removed = prev[offset:]

  return added, removed[::-1]

def closed(s):
  return s[0] + "/" + s[1:]

def solve(B, E, S):
  tag_index, raw_tags = [CHAR] * len(S), []
  matches = pattern.finditer(S)

  for m in matches:
    start, end = m.span()
    tag = S[start:end]
    tag_index[start:end] = [SKIP] * (end - start)

    if tag[1] == "/":
      tag_index[end - 1] = len(raw_tags)
    else:
      tag_index[start] = len(raw_tags)

    raw_tags.append(tag)

  text = []
  current_tags = []

  for x in range(E):
    if tag_index[x] >= 0:
      tag = raw_tags[tag_index[x]]

      if tag[1] == '/':
        current_tags.pop()
      else:
        current_tags.append(tag_index[x])

    if B <= x:
      text.append([S[x] if tag_index[x] == CHAR else '', current_tags[:]])

  text.append(['', current_tags[:]])
  result, previous = [], []

  def compare(current):
    added, removed = diff(previous, current)

    for x in removed:
      result.append(closed(raw_tags[x]))

    for x in added:
      result.append(raw_tags[x])

  for ch, current in text:
    compare(current)

    result.append(ch)
    previous = current

  compare([])

  return "".join(result)

if __name__ == '__main__':
  while True:
    data = input()
    offset = 0
    B, E = 0, 0

    if data.startswith("-1 -1"):
      break

    # B, E를 구하는 과정
    while data[offset] != ' ':
      B = B * 10 + int(data[offset])
      offset += 1

    offset += 1

    while data[offset] != ' ':
      E = E * 10 + int(data[offset])
      offset += 1

    offset += 1

    print(solve(B, E, data[offset:]))
