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


def defragment(disk_map):
    l = 0
    r = len(disk_map) - 1
    while l <= r:
        if disk_map[l] >= 0:
            l += 1
            continue
        
        if disk_map[r] < 0:
            r -= 1
            continue

        disk_map[l] = disk_map[r]
        disk_map[r] = -1
        r -= 1
        l += 1


    return disk_map

def checksum(disk_map):
    val = 0
    for i, id in enumerate(disk_map):
        val += i * id if id >= 0 else 0
    return val

print(checksum(defragment(decompress(compact_disk_map))))
