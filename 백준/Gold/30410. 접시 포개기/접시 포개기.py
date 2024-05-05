import sys
input = lambda: sys.stdin.readline().rstrip()

# 해당 수로 만들 수 있는 최대 두께를 구한다.
def calculate(count):
  result = 1
  
  while count:
    count >>= 1
    result <<= 1
    
  return result >> 1

# 인접한 1끼리, 2끼리 그룹으로 묶는다.
def group(N, A):
  groups = [A[0]]
  
  for x in range(1, N):
    if A[x - 1] != A[x]:
      groups.append(0)
    
    groups[-1] += A[x]
  
  return groups

def solve(N, A):
  G = []
  
  # 그룹 형성
  # 이때, 1 그룹이 뭉쳐 짝수가 되는 경우 인접한 2 그룹과 합친다.
  for g in group(N, A):
    if not G:
      G.append(g)
      continue
    
    if G[-1] % 2 == 0 and g % 2 == 0:
      G[-1] += g
      continue
    
    G.append(g)
    
  L = len(G)
  
  # 한 개의 그룹만 존재하는 경우
  if len(G) == 1:
    return calculate(G[0])
  
  result = 0
  
  # 1을 2로 뭉치는 과정에서 1이 하나 남는 경우가 생길 수 있다.
  # 이때, 1을 그룹을 막는 장벽이라 생각하면 다음과 같이 두 가지 케이스가 존재할 수 있다.
  
  # Case 1. [1|2...1|2]
  for x in range(1, L):
    if G[x - 1] % 2 and G[x] % 2:
      result = max(result, (G[x - 1] + G[x]) - 2)
    else:
      result = max(result, (G[x - 1] + G[x]) - 1)
  
  # Case 2. [1...2...1]
  for x in range(2, L):
    if G[x - 2] % 2 and not (G[x - 1] % 2) and G[x] % 2:
      result = max(result, (G[x - 2] + G[x - 1] + G[x]) - 2)
      
  return calculate(result)

if __name__ == "__main__":
  N = int(input())
  A = [*map(int, input().split())]
  
  print(solve(N, A))
  