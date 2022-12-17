import sys
import re

l = sys.stdin.readlines()
l = ''.join(l)

m = re.findall("[a-zA-Z0-9 \n.,'(){}\\\]+", l)
print(m)

mm = re.findall("(?P<string>[a-zA-Z0-9 \n.,'(){}\\\]+)\\\\begin\{\w}\{\d\}", l)
print(mm)