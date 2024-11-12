import sys
import re
s = sys.stdin.readlines()
s = ' '.join(s)
m = re.findall('[A-Za-z/-]+', s)
print(max(m, key=len).lower())