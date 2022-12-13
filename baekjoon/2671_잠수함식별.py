import re
p=re.compile('(100+1+|01)+')
s=input()
m=p.fullmatch(s)
print('SUBMARINE' if m else 'NOISE')