import sys

equations = open(sys.argv[1]).read().split("\n")

def check(result, operands, acc):
    if len(operands) == 0:
        return result == acc
    
    return check(result, operands[1:], acc + operands[0]) or check(result, operands[1:], acc * operands[0])

res = 0
for eq in equations:
    if eq == "":
        continue

    result, values = eq.split(": ")

    operands = list(map(int, values.split(" ")))

    if check(int(result), operands[1:], operands[0]):
        res += int(result)

print(res)