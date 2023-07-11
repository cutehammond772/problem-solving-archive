import sys
input = lambda: sys.stdin.readline().rstrip()

def convert(chars, word):
  result = 0
  
  for x in range(len(chars)):
    if chars[x] in word:
      result += (1 << x)
      
  return result

def count(N, code):
  result = 0
  
  for x in range(N):
    if code & (1 << x) > 0:
      result += 1
      
  return result

def combinations(N, R):
  combs = []
  
  for code in range(2 ** N):
    if count(N, code) == R:
      combs.append(code)
      
  return combs

def analyze(words, omit):
  result = set()
  
  for word in words:
    for ch in word:
      if (ch not in result) and (ch not in omit):
        result.add(ch)
        
  return list(result)

if __name__ == '__main__':
  N, K = map(int, input().split())
  words = [input() for _ in range(N)]
  result = 0

  chars = analyze(words, {'a', 'n', 't', 'i', 'c'})
  codes = [convert(chars, word[4:-4]) for word in words]

  if K - 5 >= len(chars):
    print(len(words))
  else:
    combs = combinations(len(chars), K - 5)
    
    for combination in combs:
      result = max(result, len([x for x in codes if (combination & x) == x]))
      
    print(result)