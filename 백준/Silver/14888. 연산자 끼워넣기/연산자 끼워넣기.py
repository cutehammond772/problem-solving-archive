# 기본 상수
ADD, SUB, MUL, DIV = "+", "-", "*", "/"

def minmax_reducer(min_init, max_init):
  min_val, max_val = max_init, min_init
  
  def resolve(val):
    nonlocal min_val, max_val
    min_val = min(min_val, val)
    max_val = max(max_val, val)
    
  def result():
    return min_val, max_val
  
  return resolve, result
    
def resolve_operators(add, sub, mul, div):
  return ([ADD] * add) + ([SUB] * sub) + ([MUL] * mul) + ([DIV] * div)

def permutation(lst, fn, snapshots, result = "", visited = None):
  if visited == None:
    visited = [False] * len(lst)

  if False not in visited:
    fn(result)
    return

  if result in snapshots:
    return
    
  snapshots.add(result)
    
  for i in range(len(lst)):
    if visited[i]:
      continue
      
    visited[i] = True
    permutation(lst, fn, snapshots, result + lst[i], visited)
    visited[i] = False
    
def solve(nums, operators):
    result = nums[0]
    
    for i in range(len(operators)):
      if operators[i] == ADD:
        result += nums[i + 1]
        
      if operators[i] == SUB:
        result -= nums[i + 1]
        
      if operators[i] == MUL:
        result *= nums[i + 1]
        
      if operators[i] == DIV:
        if result < 0 and nums[i + 1] > 0:
          result = -((-result) // nums[i + 1])
        else:
          result //= nums[i + 1]
        
    return result
  
if __name__ == "__main__":
  N = int(input())
  nums = list(map(int, input().split()))
  operators = resolve_operators(*map(int, input().split()))
  resolve, result = minmax_reducer(-1_000_000_001, 1_000_000_001)
  snapshots = set()
  
  permutation(operators, lambda ops: resolve(solve(nums, ops)), snapshots)
  
  min, max = result()
  print(max)
  print(min)