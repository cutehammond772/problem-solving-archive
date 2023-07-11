import sys
input = lambda: sys.stdin.readline().rstrip()

def find(memo, x):
  if memo[x] == x:
    return memo[x]

  traversal = [x]
  
  while memo[traversal[-1]] != traversal[-1]:
    traversal.append(memo[traversal[-1]])

  for node in traversal:
    memo[node] = traversal[-1]
    
  return memo[x]
    

def solve(G, P, planes):
  result = 0
  memo = [x for x in range(G + 1)]

  for x in planes:
    traversal = find(memo, x)
    
    if traversal == 0:
      break

    memo[traversal] = traversal - 1
    result += 1
    
  return result

if __name__ == '__main__':
  G = int(input())
  P = int(input())

  planes = [int(input()) for _ in range(P)]
  print(solve(G, P, planes))