grid = open("input").readlines()

directions = [
    (i, j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)
]
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


def count_xmas(starting_pos):
    count = 0
    for direction in directions:
        word = get_word(starting_pos, direction, 4)
        if word == "XMAS":
            count += 1
    return count


count = 0

for y, row in enumerate(grid):
    for x, letter in enumerate(row):
        if letter == "X":
            count += count_xmas((y, x))

print(count)
