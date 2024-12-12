import sys

compact_disk_map = open(sys.argv[1]).read().strip()


def decompress(compact_disk_map):
    decompressed_disk_map = []

    sector = 0

    for i, block in enumerate(compact_disk_map):
        size = int(block)
        if i % 2 == 0:
            decompressed_disk_map.extend([sector] * size)
            sector += 1
        else:
            decompressed_disk_map.extend([-1] * size)

    return decompressed_disk_map


def checksum(disk_map):
    val = 0
    for i, id in enumerate(disk_map):
        val += i * id if id >= 0 else 0
    return val


def find_space(disk_map, start, end, size):
    pointer = -1
    i = start

    while True:
        if pointer != -1 and i - pointer >= size:
            return pointer
        
        if i == end:
            return -1
        
        empty = disk_map[i] < 0

        if not empty:
            pointer = -1

        if empty and pointer == -1:
            pointer = i

        i += 1

def move_block(disk_map, from_, to, size):
    for i in range(size):
        disk_map[to + i] = disk_map[from_ + i]
        disk_map[from_ + i] = -1

def find_block_start(disk_map, index):
    id = disk_map[index]
    while disk_map[index] == id and index >= 0:
        index -= 1

    return index + 1


def defragment(disk_map):
    i = len(disk_map) - 1
    while True:
        if disk_map[i] == 0:
            break
        
        if disk_map[i] < 0:
            i -= 1
            continue

        block_start = find_block_start(disk_map, i)
        size = i - block_start + 1
        space = find_space(disk_map, 0, block_start, size)

        if space != -1:
            move_block(disk_map, block_start, space, size)

        i -= size

    return disk_map

print(checksum(defragment(decompress(compact_disk_map))))
