import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(P, Q):
  memo = [[(0, "")] * len(Q) for _ in range(len(P))]
  
  for p in range(len(P)):
    for q in range(len(Q)):
      if P[p] == Q[q]:
        if p > 0 and q > 0:
          length, result = memo[p - 1][q - 1]
          memo[p][q] = (length + 1, result + P[p])
        else:
          memo[p][q] = (1, P[p])
      else:
        candidates = [(0, "")]
        
        if p > 0:
          candidates.append(memo[p - 1][q])
          
        if q > 0:
          candidates.append(memo[p][q - 1])
          
        if p > 0 and q > 0:
          candidates.append(memo[p - 1][q - 1])

        memo[p][q] = max(candidates, key = lambda x: x[0])

  return memo[len(P) - 1][len(Q) - 1]
  
if __name__ == '__main__':
  P, Q = input(), input()
  length, result = solve(P, Q)
  
  print(length)
  
  if len(result) > 0:
    print(result)