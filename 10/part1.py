import sys

height_map = [list(map(int, line)) for line in open(sys.argv[1]).read().strip().split('\n')]

def find_trail_heads():
    trail_heads = []
    for i, row in enumerate(height_map):
        for j, height in enumerate(row):
            if height == 0:
                trail_heads.append((i, j))

    return trail_heads


def trail_head_score(head):
    m, n = len(height_map), len(height_map[0])
    reachable_summits = set()

    def walk(i, j):
        if height_map[i][j] == 9:
            reachable_summits.add((i, j))
            return
        
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and height_map[ni][nj] == height_map[i][j] + 1:
                walk(ni, nj)

    walk(head[0], head[1])

    return len(reachable_summits)

res = 0
for i, row in enumerate(height_map):
    for j, height in enumerate(row):
        if height == 0:
            res += trail_head_score((i, j))

print(res)
