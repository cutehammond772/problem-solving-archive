import sys
input = lambda: sys.stdin.readline().rstrip()

def valid(S):
	candidate = []
	
	for x in range(len(S)):
		candidate.append(S[x:len(S)] + S[:x])
	
	return min(candidate) == S

def create(S):
	# S 자체가 목걸이 수열일 때
	if valid(S):
		return f"({S})"
	
	for x in range(len(S) - 1, 0, -1):
		P, Q = S[:x], S[x:]
		
		if not valid(P):
			continue
		
		if P > Q:
			return f"({P})" + create(Q)

if __name__ == "__main__":
	S = input()
	print(create(S))
