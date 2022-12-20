import re
import sys
N=int(input())
s=''.join(sys.stdin.readlines())
of_words = ['of', 'to', 'into', 'onto', 'above', 'below', 'from', 'by', 'is', 'at']
vowels = ['a','e','i','o','u']
s = s.lower()
s = s.split()
for i in range(len(s)):
    if s[i] in of_words:
        s[i] = 'of'
for i in range(len(s)):
    cnt = sum(s[i].count(v) for v in vowels)
    cnt //= 2
    s[i] = ''.join('' if j in vowels and (cnt:=cnt-1)>-1 else j for j in s[i])
s = ' '.join(s)
s = re.sub('[,.\'"-_\?\!\[\]\{\}\(\)]', '', s)
s = re.sub('\n', ' ', s)
s = re.sub(' +', ' ', s)
tmp = 0
for i in s.split():
    print(i, end='')
    tmp+=len(i)
    if tmp>20:
        print()
        tmp=0
    else:
        print(' ', end='')
            

