import sys

garden = open(sys.argv[1]).read().strip().split("\n")
m, n = len(garden), len(garden[0])

def is_inside(i, j):
    return 0 <= i < m and 0 <= j < n

def is_outside_region(i, j, plant):
    return not is_inside(i, j) or garden[i][j] != plant


seen = set()

def explore_region(i, j, plant):
    seen.add((i, j))

    area = 1
    sides = 0

    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        adj_i, adj_j = i + di, j + dj

        if is_outside_region(adj_i, adj_j, plant):
            _i, _j = i + dj, j + di

            if not is_outside_region(_i, _j, plant) and is_outside_region(_i + di, _j + dj, plant):
                continue

            sides += 1
            continue

        if (adj_i, adj_j) in seen:
            continue

        _area, _sides = explore_region(adj_i, adj_j, plant)
        area += _area
        sides += _sides

    return area, sides


res = 0

for i in range(len(garden)):
    for j in range(len(garden[0])):
        if (i, j) in seen:
            continue

        area, sides = explore_region(i, j, garden[i][j])
        res += area * sides


print(res)
