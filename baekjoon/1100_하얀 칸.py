l = [input() for _ in range(8)]
print(sum(1 for i in range(8) for j in range(8) if (not (i+j)%2) and l[i][j]!='.'))