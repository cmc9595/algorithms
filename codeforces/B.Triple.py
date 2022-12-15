import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    input()
    l=list(map(int,input().split()))
    dic={}
    for i in l:
        dic[i] = dic.get(i, 0) + 1
        if dic[i]>=3:
            print(i)
            break
    else:
        print(-1)