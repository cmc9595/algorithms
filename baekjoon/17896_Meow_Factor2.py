import sys
import re
S=sys.stdin.readline()
m = re.search('m.+', S)
print(m)
print(m.group())