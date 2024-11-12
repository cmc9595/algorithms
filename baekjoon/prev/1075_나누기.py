N = int(input())
F = int(input())
l = []
r = N%100
while r<=100:
    tmp=N-(N%100)+r
    if tmp%F==0:
        l.append(r)
    r+=1
r = N%100
while r>=0:
    tmp=N-(N%100)+r
    if tmp%F==0:
        l.append(r)
    r-=1
print(str(min(l)).zfill(2))