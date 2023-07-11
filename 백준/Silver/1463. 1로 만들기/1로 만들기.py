N = int(input())
INTEGER_MAX = 10 ** 6 + 1

lst = [INTEGER_MAX] * (N + 1)
lst[1] = 0

for i in range(1, N + 1):
  if i + 1 <= N:
    lst[i + 1] = min(lst[i] + 1, lst[i + 1])
  if i * 2 <= N:
    lst[i * 2] = min(lst[i] + 1, lst[i * 2])
  if i * 3 <= N:
    lst[i * 3] = min(lst[i] + 1, lst[i * 3])

print(lst[N])