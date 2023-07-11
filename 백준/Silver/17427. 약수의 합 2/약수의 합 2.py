N=int(input())
print(sum(x*(N//x)for x in range(1,N+1)))