x1,y1=map(int, input().split())
x2,y2=map(int, input().split())
x3,y3=map(int, input().split())
a = (x2-x1, y2-y1)
b = (x3-x2, y3-y2)
val = b[1]*a[0] - b[0]*a[1]
if val>0:
    print(1)
elif val==0:
    print(0)
else:
    print(-1)