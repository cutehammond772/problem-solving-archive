N = int(input())

lst = [0] * (N + 1)

for i in range(1, N + 1):
  if i == 1:
    lst[i] = 1
  elif i == 2:
    lst[i] = 2
  else:
    lst[i] = lst[i - 1] + lst[i - 2]

print(lst[N] % 10007)