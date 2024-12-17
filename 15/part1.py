import sys

warehouse, moves = open(sys.argv[1]).read().split("\n\n")
m = [list(line) for line in warehouse.split('\n')]


def find_robot():
    for i,row in enumerate(m):
        for j, v in enumerate(row):
            if v == '@':
                return (i, j)
    
    raise ValueError('robot not found')

def spot(pos):
    return m[pos[0]][pos[1]]

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

vel_map = {
    'v': (1, 0),
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
}

def move(pos, vel):
    next_pos = add(pos, vel)

    p = next_pos
    while spot(p) == 'O':
        p = add(p, vel)

    if spot(p) == '#':
        return pos
    
    m[p[0]][p[1]] = 'O'
    m[next_pos[0]][next_pos[1]] = '@'
    m[pos[0]][pos[1]] = '.'

    return next_pos


def simulate(pos, moves):
    for dir in moves:
        pos = move(pos, vel_map[dir])

simulate(find_robot(), moves.replace('\n', ''))

res = 0

for i, row in enumerate(m):
    for j, v in enumerate(row):
        if v == 'O':
            res += i * 100 + j

print(res)





