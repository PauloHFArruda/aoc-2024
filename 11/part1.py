import sys

stones = list(map(int, open(sys.argv[1]).read().strip().split(' ')))

def apply_rules(stone):
    if stone == 0:
        return [1]
    
    str_val = str(stone)

    if len(str_val) % 2 == 0:
        return [int(str_val[:len(str_val) // 2]), int(str_val[len(str_val) // 2:])]
    
    return [stone*2024]
        


def blink(stones):
    result = []
    for stone in stones:
        result.extend(apply_rules(stone))
    return result

for i in range(25):
    stones = blink(stones)

print(len(stones))