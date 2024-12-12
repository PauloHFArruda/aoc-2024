import sys
from functools import lru_cache

stones = list(map(int, open(sys.argv[1]).read().strip().split(' ')))

@lru_cache(maxsize=None)
def blink(stone, blinks):
    if blinks == 0:
        return 1

    if stone == 0:
        return blink(1, blinks - 1)
    
    str_val = str(stone)

    if len(str_val) % 2 == 0:
        return blink(int(str_val[:len(str_val) // 2]), blinks - 1) + blink(int(str_val[len(str_val) // 2:]), blinks - 1)
    
    return blink(stone*2024, blinks - 1)


total = 0
for stone in stones:
    total += blink(stone, 75)

print(total)