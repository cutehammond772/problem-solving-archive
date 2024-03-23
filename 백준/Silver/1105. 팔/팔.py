import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(L, R):
  result = 0
  
  if len(L) != len(R):
    return result
  
  for i in range(len(L)):
    if L[i] != R[i]:
      return result
    
    result += (L[i] == '8')
  
  return result

if __name__ == "__main__":
  L, R = input().split()
  print(solve(L, R))
