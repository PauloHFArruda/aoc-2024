import sys

lab_map = [list(row.strip()) for row in open(sys.argv[1]).readlines()]


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


def check_loop(pos, vel, seen):
    while True:
        if (pos, vel) in seen:
            return True

        seen.add((pos, vel))

        if not is_inside(move(pos, vel)):
            return False

        while spot(move(pos, vel)) == "#":  # assumes not started in the right border
            vel = rotate(vel)

        pos = move(pos, vel)


pos = find_guard()
vel = (-1, 0)

seen_poses = set()
seen_pos = set()

new_obstacles = set()

while True:
    if (pos, vel) in seen_poses:
        break

    if not is_inside(move(pos, vel)):
        break

    while spot(move(pos, vel)) == "#":  # assumes not started in the right border
        vel = rotate(vel)

    next_pos = move(pos, vel)
    if not next_pos in seen_pos:
        lab_map[next_pos[0]][next_pos[1]] = "#"
        if check_loop(pos, vel, seen_poses.copy()):
            new_obstacles.add(next_pos)
        lab_map[next_pos[0]][next_pos[1]] = "."

    seen_poses.add((pos, vel))
    seen_pos.add(pos)

    pos = next_pos

print(len(new_obstacles))
