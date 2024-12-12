import sys

height_map = [list(map(int, line)) for line in open(sys.argv[1]).read().strip().split('\n')]

def find_trail_heads():
    trail_heads = []
    for i, row in enumerate(height_map):
        for j, height in enumerate(row):
            if height == 0:
                trail_heads.append((i, j))

    return trail_heads


def trail_head_rating(head):
    m, n = len(height_map), len(height_map[0])
    rating = 0

    def walk(i, j):
        nonlocal rating
        if height_map[i][j] == 9:
            rating += 1
            return
        
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and height_map[ni][nj] == height_map[i][j] + 1:
                walk(ni, nj)

    walk(head[0], head[1])

    return rating

res = 0
for i, row in enumerate(height_map):
    for j, height in enumerate(row):
        if height == 0:
            res += trail_head_rating((i, j))

print(res)
