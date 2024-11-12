N, M = map(int, input().split())
l = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x:x[1])
print(l)