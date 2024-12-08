import sys

lab_map = [row.strip() for row in open(sys.argv[1]).readlines()]


def find_guard():
    for i, row in enumerate(lab_map):
        for j, cell in enumerate(row):
            if cell == "^":
                return i, j

    raise ValueError("Guard not found")


def move(pos, vel):
    return (pos[0] + vel[0], pos[1] + vel[1])


def rotate(vel):
    return (vel[1], -vel[0])


def spot(pos):
    return lab_map[pos[0]][pos[1]]


def is_inside(pos):
    return 0 <= pos[0] < len(lab_map) and 0 <= pos[1] < len(lab_map[0])


pos = find_guard()
vel = (-1, 0)

visited = {}

while True:
    if pos in visited and vel in visited[pos]:
        break

    visited[pos] = visited.get(pos, set())
    visited[pos].add(vel)

    if not is_inside(move(pos, vel)):
        break

    while spot(move(pos, vel)) == "#":  # assumes not started in the right border
        vel = rotate(vel)

    pos = move(pos, vel)

print(len(visited))
