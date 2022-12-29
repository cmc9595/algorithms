import re
P = int(input())
l = [input() for _ in range(P)]
for line in l:
    line = re.sub('s(?=[^A-Za-z]+)', 'S', line) # (?=string) 전방탐색
    line = re.sub('s$', 'S', line)
    line = re.sub('sf', 'Sf', line)
    line = re.sub('sb', 'Sb', line)
    line = re.sub('sk', 'Sk', line)
    if re.search('sss', line):
        line = re.sub('sss', 'sSs', line)
        line = re.sub('s', '[longs]', line)
        line = re.sub('(ssi|si|sh|sl|st|ss)', r'[long\1]', line)
    else:
        line = re.sub('sss', 'sSs', line)
        line = re.sub('(ssi|si|sh|sl|st|ss|s)', r'[long\1]', line)

    line = re.sub('S', 's', line)
    line = re.sub('(AE|Ae)', '[AE]', line)
    line = re.sub('(aE|ae)', '[ae]', line)
    line = re.sub('(OE|Oe)', '[OE]', line)
    line = re.sub('(oE|oe)', '[oe]', line)
    line = re.sub('(ct|ffi|ffl|ff|fi|fl)', r'[\1]', line)
    print(line)

    # 반례: crosstitch, crosstaff