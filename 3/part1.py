import re

multiplication_values = re.compile(r'mul\((\d*),(\d*)\)').findall(open('input').read())

print(sum(map(lambda x: int(x[0]) * int(x[1]), multiplication_values)))