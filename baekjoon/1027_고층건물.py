N = int(input())
l = list(map(int, input().split()))

def check(a, b): # a에서 b가 보이는지 판단 - 항상 a < b, l[a] ? l[b]
    d = (l[b]-l[a])/(b-a) # 기울기 -> 소수점문제
    cur = l[a]
    for i in range(a+1, b):
        # cur += d
        # if cur <= l[i]
        if l[a]*(b-a) + (l[b]-l[a])*(i-a) <= l[i]*(b-a): # 가려짐
            return 0
    else:
        return 1
# cur = l[a] + (l[b]-l[a])/(b-a)*i <= l[i]
# cur*(b-a) = l[a]*(b-a) + (l[b]-l[a])*i
# (cur-l[a])*(b-a) = (l[b]-l[a])*i
answer=[]
for i in range(N):
    cnt = 0
    for j in range(N):
        if i==j:
            continue
        cnt += check(i, j) if i < j else check(j, i)
        # print(i, j, check(i, j))
    answer.append(cnt)
print(max(answer))