import sys
import heapq
input=sys.stdin.readline
V, E = map(int, input().split())
# Primm
graph=[[] for _ in range(V+1)]
v=[False]*(V+1)
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
# start_node = 1
v[0]=True
q=[(0, 1)]
total=0
while q:
    val, cur = heapq.heappop(q)
    if v[cur]:
        continue
    v[cur] = True
    total += val
    for nxt, nval in graph[cur]:
        if not v[nxt]:
            heapq.heappush(q, (nval, nxt))
print(total)