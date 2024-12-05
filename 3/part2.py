import re

instructions = re.compile(r'(do\(\))|(don\'t\(\))|mul\((\d*),(\d*)\)').findall(open('input').read())

active = True
res = 0
for instruction in instructions:
    do, dont, a, b = instruction

    if do:
        active = True
        continue

    if dont:
        active = False
        continue
    
    res += int(a) * int(b) if active else 0

print(res)