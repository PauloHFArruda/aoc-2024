grid = open('input').readlines()

limits = (len(grid), len(grid[0]))


def move(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def is_inside(pos):
    return 0 <= pos[0] < limits[0] and 0 <= pos[1] < limits[1]


def get_word(pos, direction, size):
    word = ""
    while is_inside(pos) and len(word) < size:
        word += grid[pos[0]][pos[1]]
        pos = move(pos, direction)
    return word


def is_mas(word):
    return word == "MAS" or word == "SAM"


def is_x_mas(a_pos):
    if letter != "A":
        return 0

    return is_mas(get_word(move(a_pos, (-1, -1)), (1, 1), 3)) and is_mas(
        get_word(move(a_pos, (-1, 1)), (1, -1), 3)
    )


count = 0

for y, row in enumerate(grid):
    for x, letter in enumerate(row):
        count += is_x_mas((y, x))

print(count)
