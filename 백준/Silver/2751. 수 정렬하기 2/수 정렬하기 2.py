import sys
input = sys.stdin.readline
arr = []

for i in range(int(input().strip())):
  arr.append(int(input().strip()))
  
for i in sorted(arr):
  print(i)