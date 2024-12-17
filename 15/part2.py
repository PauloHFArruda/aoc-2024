import sys
from functools import reduce

warehouse, moves = open(sys.argv[1]).read().split("\n\n")
warehouse = [list(line) for line in warehouse.split("\n")]

wider_mapping = {"#": ["#", "#"], ".": [".", "."], "@": ["@", "."], "O": ["[", "]"]}
m = [reduce(lambda acc, v: acc + wider_mapping[v], row, []) for row in warehouse]

def find_robot():
    for i, row in enumerate(m):
        for j, v in enumerate(row):
            if v == "@":
                return (i, j)

    raise ValueError("robot not found")


def spot(pos):
    return m[pos[0]][pos[1]]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


vel_map = {
    "v": (1, 0),
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
}


def can_move_box_x(pos, vel):
    next_pos = add(pos, vel)
    next_box_pos = add(next_pos, vel)

    c = spot(next_box_pos if vel == (0, 1) else next_pos)

    if c == "#":
        return False

    if c == ".":
        return True


    return can_move_box_x(next_box_pos, vel)

def can_move_box_y(pos, vel):
    p1 = add(pos, vel)
    p2 = add(p1, (0, 1))

    c1 = spot(p1)
    c2 = spot(p2)

    if c1 == "#" or c2 == "#":
        return False

    if c1 == "." and c2 == ".":
        return True

    if c1 == "[":
        return can_move_box(p1, vel)

    r1 = can_move_box_y(add(p1, (0, -1)), vel) if c1 == "]" else True
    r2 = can_move_box_y(p2, vel) if c2 == "[" else True

    return r1 and r2

def can_move_box(pos, vel):
    if vel[0] == 0:
        return can_move_box_x(pos, vel)

    return can_move_box_y(pos, vel)


def update_box_pos(pos, next_pos):
    m[pos[0]][pos[1]] = "."
    m[pos[0]][pos[1] + 1] = "."
    m[next_pos[0]][next_pos[1]] = "["
    m[next_pos[0]][next_pos[1] + 1] = "]"


def move_box_x(pos, vel):
    next_pos = add(pos, vel)

    next_box_pos = add(next_pos, vel)

    if next_box_pos[1] < 0:
        print(pos, next_box_pos)
        print('\n'.join(''.join(row) for row in m))
        return

    if spot(next_box_pos) == "[":
        move_box_x(next_box_pos, vel)

    update_box_pos(pos, next_pos)


def move_box_y(pos, vel):
    p1 = add(pos, vel)
    p2 = add(add(pos, (0, 1)), vel)

    if spot(p1) == "[":
        move_box(p1, vel)

    if spot(p1) == "]":
        move_box(add(p1, (0, -1)), vel)

    if spot(p2) == "[":
        move_box(p2, vel)

    update_box_pos(pos, p1)

def move_box(pos, vel):
    if vel[0] == 0:
        return move_box_x(pos, vel)

    move_box_y(pos, vel)


def update_robot_pos(pos, next_pos):
    m[next_pos[0]][next_pos[1]] = "@"
    m[pos[0]][pos[1]] = "."


def move(pos, vel):
    next_pos = add(pos, vel)

    if spot(next_pos) == "#":
        return pos

    if spot(next_pos) == ".":
        update_robot_pos(pos, next_pos)
        return next_pos

    box_pos = add(next_pos, (0, -1)) if spot(next_pos) == "]" else next_pos

    if not can_move_box(box_pos, vel):
        return pos

    move_box(box_pos, vel)
    update_robot_pos(pos, next_pos)
    return next_pos


def simulate(pos, moves):
    for dir in moves:
        pos = move(pos, vel_map[dir])

simulate(find_robot(), moves.replace("\n", ""))

res = 0

for i, row in enumerate(m):
    for j, v in enumerate(row):
        if v == "[":
            res += i * 100 + j

print(res)
