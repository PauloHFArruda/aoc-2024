import sys
import re
from functools import lru_cache

A_COST = 3
B_COST = 1
INF =  1 << 60

def getMachineInfo(data):
    ax, ay, bx, by, tx, ty = map(int, re.findall(r"\d+", data))

    return (ax, ay), (bx, by), (tx, ty)

def sub(a, b):
    return a[0] - b[0], a[1] - b[1]

@lru_cache(maxsize=None)
def solve(a, b, t, moves):
    if t == (0, 0):
        return 0

    if moves == 0:
        return INF
    
    if t[0] < 0 or t[1] < 0:
        return INF

    return min(
        solve(a, b, sub(t, a), moves - 1) + A_COST,
        solve(a, b, sub(t, b), moves - 1) + B_COST,
    )


machines = [getMachineInfo(data) for data in open(sys.argv[1]).read().strip().split("\n\n")]
total = 0

for a, b, t in machines:
    tokens = solve(a, b, t, 200)
    if tokens < INF:
        total += tokens

print(total)
