import sys
sys.setrecursionlimit(101010)
input = lambda: sys.stdin.readline().rstrip()

def solve(S, T):
	if len(S) == len(T):
		return 1 if (S == T) else 0
	
	if T[-1] == 'A':
		return solve(S, T[:len(T) - 1])
	else:
		return solve(S, T[:len(T) - 1][::-1])

if __name__ == "__main__":
	S, T = input(), input()
	print(solve(S, T))
	