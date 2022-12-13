import re
K = int(input())
inputs = [[input(), input()] for _ in range(K)]
ans = []
for i, (s1, s2) in enumerate(inputs):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = re.sub('[\(\)\[\]\{\}.,;:]', ' ', s1)
    s2 = re.sub('[\(\)\[\]\{\}.,;:]', ' ', s2)
    l1 = s1.split()
    l2 = s2.split()
    ans.append(f"Data Set {i+1}: {'equal' if l1==l2 else 'not equal'}")
print(*ans, sep='\n\n')