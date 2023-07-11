N = int(input())
M = int(input())
S = input()

stack, count = 0, 0
for i in range(M):
  if S[i] == 'I':
    if i < M - 2 and S[i + 1] == 'O' and S[i + 2] == 'I':
      stack += 1
      i += 1
      
      if stack >= N:
        count += 1
    else:
      stack = 0

print(count)