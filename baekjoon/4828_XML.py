import sys
import re
context = []
l = sys.stdin.readlines()
for s in l:
    m = re.findall('((<.+>)+?)|((</.+>)+?)', s)
    print(m)
    # s = re.sub('[&lt;]', '<')
    # s = re.sub('[&gt;]', '>')
    # s = re.sub('[&amp;]', '&')
    
