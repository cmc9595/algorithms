import sys
import re
l = sys.stdin.readlines()
for line in l:
    if line=='END\n':
        break
    m = re.fullmatch('\"(?P<string>[A-Za-z\s]*)\"\s(?P=string)\n', line) # 같은 문자열 찾는 조건주기
    print(f'Quine({m.group("string")})' if m else 'not a quine')