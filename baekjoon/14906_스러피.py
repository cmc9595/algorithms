import re
N=int(input())
l=[input() for _ in range(N)]
print('SLURPYS OUTPUT')

def isSlump(s):
    return True if re.fullmatch('([D|E]F+)+G', s) else False

def isSlimp(s):
    if len(s)==2:
        if s=='AH':
            return True
        return False
    elif len(s)>=3:
        if s[:2]=='AB' and isSlimp(s[2:-1]) and s[-1]=='C':
            return True
        if s[0]=='A' and isSlump(s[1:-1]) and s[-1]=='C':
            return True
        return False

for s in l:
    for i in range(2, len(s)-2):
        s1, s2 = s[:i], s[i:]
        # print(s1, s2, isSlimp(s1), isSlump(s2))
        if isSlimp(s1) and isSlump(s2):
            print('YES')
            break
    else:
        print('NO')
print('END OF OUTPUT')