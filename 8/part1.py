import sys
from collections import defaultdict

antennas_map = open(sys.argv[1]).read().strip().split("\n")

antennas_pos_by_freq = defaultdict(list)

for i, row in enumerate(antennas_map):
    for j, cell in enumerate(row):
        if cell != ".":
            antennas_pos_by_freq[cell].append((i, j))

antennas_pairs = []

for positions in antennas_pos_by_freq.values():
    for i, pos1 in enumerate(positions):
        for pos2 in positions[i + 1 :]:
            antennas_pairs.append((pos1, pos2))


def is_inside(pos):
    return 0 <= pos[0] < len(antennas_map) and 0 <= pos[1] < len(antennas_map[0])

def add(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

def neg(pos):
    return (-pos[0], -pos[1])

antinodes = set()

for pair in antennas_pairs:
    pos1, pos2 = pair
    diff = add(pos2, neg(pos1))
    antinode1 = add(pos1, neg(diff))
    antinode2 = add(pos2, diff)

    if is_inside(antinode1):
        antinodes.add(antinode1)

    if is_inside(antinode2):
        antinodes.add(antinode2)

print(len(antinodes))
