import re
# p = re.compile('(A|B|C|D|E|F){0,1}A+F+C+(A|B|C|D|E|F){0,1}')
p = re.compile('[A-F]?A+F+C+[A-F]?')
T = int(input())
for _ in range(T):
    s = input()
    mm = p.fullmatch(s)
    print('Infected!' if mm else 'Good')