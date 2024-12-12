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
    perimeter = 0

    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        adj_i, adj_j = i + di, j + dj

        if is_outside_region(adj_i, adj_j, plant):
            perimeter += 1
            continue

        if (i, j) in seen:
            continue

        _area, _perimeter = explore_region(adj_i, adj_j, plant)
        area += _area
        perimeter += _perimeter

    return area, perimeter


res = 0

for i in range(len(garden)):
    for j in range(len(garden[0])):
        if (i, j) in seen:
            continue

        area, perimeter = explore_region(i, j, garden[i][j])
        res += area * perimeter

print(res)
