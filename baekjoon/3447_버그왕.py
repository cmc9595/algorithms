import re
import sys
s = sys.stdin.readlines()
s = ''.join(s)
while tmp:=re.sub('BUG', '', s):
    if tmp==s:
        break
    s = tmp
print(tmp)
