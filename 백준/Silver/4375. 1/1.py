import sys, math
input = lambda: sys.stdin.readline().rstrip()

def solve(T):
  L, N = len(T), int(T)

  # T 자체가 1로만 이루어진 수일 때
  if T == '1' * L:
    return L

  offset = math.ceil(math.log10(N))
  modular = int('1' * offset)
  
  while modular % N > 0:
    modular = 10 * (modular % N) + 1
    offset += 1

  return offset

if __name__ == '__main__':
  # 테스트 케이스
  while (T := input()):
    print(solve(T))
