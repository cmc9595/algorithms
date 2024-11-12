import sys
import re
from collections import defaultdict
l = ''.join(sys.stdin.readlines())
cites = re.findall('\\\\cite{(\w+)}', l)
bibs = re.findall('\\\\bibitem{(?P<author>\w+)}(?P<line>.+)', l)
bibs = dict(bibs)
if cites==list(bibs.keys()):
    print('Correct')
else:
    print('Incorrect')
    mm = re.search('\\\\begin{.+}{.+}.+\\\\end{.+}', l, flags=re.DOTALL)
    mm = mm.group().split('\n')
    res = [mm[0]]
    for cite in cites:
        res.append(f'\\bibitem{{{cite}}}{bibs[cite]}')
    res.append(mm[-1])
    print('\n'.join(res))