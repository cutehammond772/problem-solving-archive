import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
  stack, popped = [], []
  
  def make(offset):
    if stack:
      popped.append(stack.pop())
      make(offset)
      stack.append(popped.pop())

    if offset > N:
      if not stack:
        print(*popped)
        
      return
      
    stack.append(offset)
    make(offset + 1)
    stack.pop()

  make(1)

if __name__ == '__main__':
  N = int(input())
  solve(N)