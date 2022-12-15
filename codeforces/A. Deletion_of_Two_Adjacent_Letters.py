t=int(input())
for _ in range(t):
    s = input()
    c = input()
    indices = [i for i in range(len(s)) if s[i]==c]
    # print(indices)
    if not indices:
        print('NO')
        continue
    else:
        for i in indices:
            l = i
            r = len(s)-1-i
            if l%2==0 or r%2==0:
                print('YES')
                break
        else:
            print('NO')