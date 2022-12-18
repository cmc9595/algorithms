import re
s = input()
l = re.findall('(?=([A-Z][a-z]*[A-Z]))', s)
cnt=0
for i in l:
    j = len(i)-2
    if j==3:
        continue
    elif j<4:
        cnt += 3-j
    else:
        cnt += 4*(j//4 + 1) - 1 - j
print(cnt)