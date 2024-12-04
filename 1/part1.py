data = [list(map(int, line.split())) for line in open('input').readlines()]

groups = [sorted([row[i] for row in data]) for i in range(2)]

res = sum(map(lambda x: abs(x[0] - x[1]), zip(*groups)))

print(res)