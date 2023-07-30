import sys
input = lambda: sys.stdin.readline().rstrip()

def create(P):
  table = [0] * len(P)
  pf, sf = 0, 1

  while sf < len(P):
    if P[pf] == P[sf]:
      pf += 1
      table[sf] = pf
      sf += 1

    else:
      if pf:
        pf = table[pf - 1]
      else:
        table[sf] = 0
        sf += 1

  return table

# kmp 알고리즘 이용
def solve(T, P):
  result = []

  table = create(P)
  idx, offset = 0, 0

  LP, LT = len(P), len(T)

  while idx < LT:
    if P[offset] == T[idx]:
      idx += 1
      offset += 1

      if offset == LP:
        result.append(idx - offset + 1)
        offset = table[offset - 1]
    else:
      if offset:
        offset = table[offset - 1]
      else:
        idx += 1

  return result

if __name__ == '__main__':
  T, P = input(), input()
  result = solve(T, P)

  print(len(result))

  if result:
    print(*result)
