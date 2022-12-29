N, M = map(int, input().split())
l=[list(map(int, list(input()))) for _ in range(N)]
answer=1
for n in range(2, N+1):
    for i in range(N-n+1):
        for j in range(M-n+1):
            if l[i][j]==l[i+n-1][j]==l[i][j+n-1]==l[i+n-1][j+n-1]:
                answer=n*n          
print(answer)