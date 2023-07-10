import sys
input = lambda: sys.stdin.readline().rstrip()

def create(N):
  tries = {}
  
  for _ in range(N):
    K, *maps = input().split()
    current = tries
    
    for x in range(int(K)):
      if maps[x] not in current:
        current[maps[x]] = {}
        
      current = current[maps[x]]
  
  return tries

def visualize(tries):
  result = []
  
  def traverse(T, depth):
    for root in sorted(T.keys()):
      result.append(("--" * depth) + root)
      traverse(T[root], depth + 1)
      
  traverse(tries, 0)
  return result

if __name__ == '__main__':
  N = int(input())
  tries = create(N)
  
  result = visualize(tries)
  print(*result, sep='\n')
  