import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
  dict = {}
  
  for _ in range(N):
    data = input()
    L = len(data)
    
    for x in range(L):
      if data[x] not in dict:
        dict[data[x]] = 0
        
      dict[data[x]] += 10 ** ((L - 1) - x)
  
  values = sorted(dict.values(), reverse=True)
  return sum([(9 - x) * values[x] for x in range(len(values))])

if __name__ == '__main__':
  N = int(input())
  print(solve(N))
  
  
