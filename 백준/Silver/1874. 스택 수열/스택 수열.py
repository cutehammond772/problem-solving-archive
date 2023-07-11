import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
seq = [int(input().strip()) for _ in range(N)]
asc_seq = sorted(seq)
stack = []
commends = []
seq_off, asc_off = 0, 0

while seq_off < N:
  if len(stack) == 0:
    stack.append(asc_seq[asc_off])
    commends.append('+')
    asc_off += 1
  elif seq[seq_off] != stack[-1]:
    if asc_off == N:
      print("NO")
      break
    
    stack.append(asc_seq[asc_off])
    commends.append('+')
    asc_off += 1
  else:
    stack = stack[:-1]
    commends.append('-')
    seq_off += 1

if seq_off == N:
  for cmd in commends:
    print(cmd + '\n')