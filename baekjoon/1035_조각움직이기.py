from itertools import combinations, permutations
l=[input() for _ in range(5)]
cnt=0
origin=[]
for i in range(5):
    for j in range(5):
        if l[i][j]=='*':
            cnt+=1
            origin.append((i, j))

dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def is_connected(coords):
    s = set(coords)
    coords = set(coords)
    start = coords.pop()
    q = [start]
    visit = set()
    visit.add(start)
    while q:
        y, x = q.pop()
        for dy, dx in dr:
            ny = y+dy
            nx = x+dx
            if 0<=ny<=4 and 0<=nx<=4 and ((ny,nx) in coords) and ((ny, nx) not in visit):
                visit.add((ny, nx))
                q.append((ny, nx))
    return True if visit==s else False

def calculate_diff(origin, coords):
    tmp=[]
    for i in permutations(coords):
        tmp.append(sum(abs(y1-y2)+abs(x1-x2) for (y1,x1), (y2,x2) in zip(origin, i)))
    return min(tmp)

ans=[]
for coords in combinations([(i, j) for i in range(5) for j in range(5)], cnt):
    if is_connected(coords):
        ans.append(calculate_diff(origin, coords))
print(min(ans))