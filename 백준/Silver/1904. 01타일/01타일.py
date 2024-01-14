N = int(input())
x, y, z = 1, 1, 1

for i in range(2, N + 1):
  z = (x + y) % 15746
  x, y = y % 15746, z

print(z)