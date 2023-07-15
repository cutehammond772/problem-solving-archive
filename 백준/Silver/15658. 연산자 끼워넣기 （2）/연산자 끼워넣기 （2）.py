import sys
input = lambda: sys.stdin.readline().rstrip()
ADD, SUB, MUL, DIV = 0, 1, 2, 3

def solve(N, nums, ops):
  max_result, min_result = -10 ** 10, 10 ** 10
  
  def permutation(offset, total):
    nonlocal max_result, min_result
    
    if offset >= N:
      max_result = max(max_result, total)
      min_result = min(min_result, total)
      return
    
    for op in range(4):
      if ops[op]:
        ops[op] -= 1
        next = total
        
        if op == ADD:
          next += nums[offset]
        elif op == SUB:
          next -= nums[offset]
        elif op == MUL:
          next *= nums[offset]
        elif op == DIV:
          if next < 0:
            next = -(-next // nums[offset])
          else:
            next //= nums[offset]
        
        permutation(offset + 1, next)
        ops[op] += 1
  
  permutation(1, nums[0])
  return max_result, min_result

if __name__ == '__main__':
  N = int(input())
  nums = [*map(int, input().split())]
  ops = [*map(int, input().split())]
  
  max_result, min_result = solve(N, nums, ops)
  
  print(max_result)
  print(min_result)
  