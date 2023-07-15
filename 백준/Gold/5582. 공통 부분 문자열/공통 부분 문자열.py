import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  P, Q = input(), input()
  memo = [[0] * (len(Q) + 1) for _ in range(len(P) + 1)]
  result = 0
  
  for px in range(len(P)):
    for qx in range(len(Q)):
      if P[px] != Q[qx]:
        continue
        
      memo[px][qx] = memo[px - 1][qx - 1] + 1
      result = max(result, memo[px][qx])
  
  print(result)
  