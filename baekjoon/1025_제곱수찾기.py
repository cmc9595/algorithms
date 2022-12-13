N, M = map(int, input().split())
def isSquare(n):
    return True if n**0.5 == int(n**0.5) else False
def getSeq(y, x, dy, dx):
    num=l[y][x]
    while 0<=y+dy<N and 0<=x+dx<M:
        y += dy
        x += dx
        num+=l[y][x]
        yield int(num)
    yield int(num)
l = [list(input()) for _ in range(N)]
steps = set((y, x) for y in range(N) for x in range(M))
nums = set()
drs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
for i in range(N):
    for j in range(M):
        for step in steps:
            if step==(0, 0):
                if isSquare(int(l[i][j])):
                    nums.add(int(l[i][j]))
            else:
                for dr in drs:
                    dy = step[0]*dr[0]
                    dx = step[1]*dr[1]
                    for seq in getSeq(i, j, dy, dx):
                        if isSquare(seq):
                            nums.add(seq)
print(max(nums) if nums else -1)