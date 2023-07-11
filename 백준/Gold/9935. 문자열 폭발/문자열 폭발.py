import sys
input = lambda: sys.stdin.readline().strip()

word, bomb = input(), input()

# (char, streak)
stack = [('', -1)]

for idx in range(len(word)):
  chr = word[idx]
  _, streak = stack[-1]
  next = streak + 1
  
  # add character to stack
  if bomb[next] == chr:
    stack.append((chr, next))
    
    if len(bomb) == next + 1:
      for _ in range(len(bomb)):
        stack.pop()
      
  else:
    stack.append((chr, -1 if bomb[0] != chr else 0))

result = ''.join(map(lambda x: x[0], stack))

if len(result) == 0:
  print("FRULA")
else:
  print(result)