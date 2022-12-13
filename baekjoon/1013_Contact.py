import re
p = re.compile('(100+1+|01)+') # *,+: 탐욕, +?,*?: 비탐욕
T = int(input())
for _ in range(T):
    s = input()
    print('YES' if (m:=p.fullmatch(s)) and m.group()==s else 'NO')