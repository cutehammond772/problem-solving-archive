print(*map(lambda t: f'{t[0]} {t[1]}', sorted([tuple(map(int, input().split())) for _ in range(int(input()))])), sep='\n')