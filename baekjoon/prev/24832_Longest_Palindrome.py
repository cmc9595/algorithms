n, m = map(int, input().split())
l = set([input() for _ in range(n)])
v=[False]*n
pal=[]
while l:
    tmp = l.pop()
    if tmp[::-1] in l:
        l.remove(tmp[::-1])
        pal=[tmp]+pal+[tmp[::-1]]
    elif tmp==tmp[::-1] and len(pal)%2==0:
         pal=pal[:len(pal)//2]+[tmp]+pal[len(pal)//2:]
print(n:=len(pal:=''.join(pal)))
if n>0:
    print(pal)
# for i in range(n//2):
#     if l[i]==l[n-1-i][:d:-1]:
#         pal=[l[i]]+pal+[l[n-1-i]]
#     elif l[i]==l[i][::-1] and len(pal)%2==0:
#         pal=pal[:len(pal)//2]+[l[i]]+pal[len(pal)//2:]
# print(n:=len(pal:=''.join(pal)))
# if n>0:
#     print(pal)