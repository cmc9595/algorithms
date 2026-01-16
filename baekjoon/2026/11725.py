import sys
from collections import deque

# input = sys.stdin.readline

N = int(sys.stdin.readline())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]


# 인접행렬 대신, 인접 리스트를 써야한다.
# G = [[0 for _ in range(N+1)] for _ in range(N+1)]
# for i, j in L:
#     G[i][j] = 1
#     G[j][i] = 1
G = [[] for _ in range(N+1)]
for i, j in L:
    G[i].append(j)
    G[j].append(i)


start = 1
visited = [False for _ in range(N+1)]
parent = [0 for _ in range(N+1)]
q = deque([start])
visited[start] = True
while q:
    cur = q.popleft()
    for nxt in G[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)
            parent[nxt] = cur

for i in parent[2:]:
    print(i)