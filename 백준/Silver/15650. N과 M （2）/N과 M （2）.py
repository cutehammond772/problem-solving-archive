import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M):
  result = []
  temp = []

  def make(offset, count):
    if count == M:
      result.append(tuple(temp))
      return

    for k in range(offset, N + 1):
      temp.append(k)
      make(k + 1, count + 1)
      temp.pop()
      
  make(1, 0)
  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  
  for combination in solve(N, M):
    print(*combination)