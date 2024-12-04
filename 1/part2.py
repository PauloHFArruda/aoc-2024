from functools import reduce

data = [list(map(int, line.split())) for line in open('input').readlines()]

groups = [[row[i] for row in data] for i in range(2)]

def freq(data_list, value):
    return reduce(lambda acc, e: acc + (e == value), data_list, 0)

res = sum(map(lambda x: x*freq(groups[1], x), groups[0]))

print(res)