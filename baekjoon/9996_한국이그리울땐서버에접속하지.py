import re
N=int(input())
pattern=input()
pattern=pattern.replace('*', '[a-z]*')
p=re.compile(pattern)
for _ in range(N):
    s=input()
    m=p.fullmatch(s)
    print('DA' if m else 'NE')