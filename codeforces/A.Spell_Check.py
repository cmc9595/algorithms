import sys
from collections import Counter

input = sys.stdin.readline
name = Counter('Timur\n')
for _ in range(int(input())):
    input()
    print('YES' if name==Counter(input()) else 'NO')