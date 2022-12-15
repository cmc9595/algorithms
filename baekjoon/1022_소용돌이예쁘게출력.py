r1,c1,r2,c2 = map(int, input().split())
l = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

dr = [(0, 1), (-1, 0), (0, -1), (1, 0)] #(y, x), 우상좌하순
y=x=0
num=1
d=0
row_len=1
row_cnt=0
total = (c2-c1+1)*(r2-r1+1)

while total > 0:
    if r1<=y<=r2 and c1<=x<=c2:
        l[y-r1][x-c1] = num
        total -=1
        
    y+=dr[d][0]
    x+=dr[d][1]
    
    row_cnt+=1
    if row_cnt==row_len:
        d=(d+1)%4
        row_cnt=0
        if d==0 or d==2:
            row_len+=1      
    num+=1

max_len = len(str(num))
for r in l:
    for c in r:
        print(str(c).rjust(max_len, ' '), end=' ')
    print()