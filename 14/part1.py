import sys
from functools import reduce

WIDTH = 101
HEIGHT = 103

def get_robot_pose(data):
    p, v = data.split(" ")

    px, py = p.split("=")[1].strip().split(",")
    vx, vy = v.split("=")[1].strip().split(",")

    return ((int(px), int(py)), (int(vx), int(vy)))

def move_robot(pose):
    ((px, py), (vx, vy)) = pose

    return (((px+vx)%WIDTH, (py+vy)%HEIGHT), (vx, vy))

robots = [get_robot_pose(data) for data in open(sys.argv[1]).read().strip().split("\n")]

middle_x = WIDTH//2
middle_y = HEIGHT//2

robots_by_quadrant = {}

for pose in robots:
    for _ in range(100):
        pose = move_robot(pose)

    ((px, py), _) = pose

    if px == middle_x or py == middle_y:
        continue

    quadrant = 1

    if px > middle_x:
        quadrant += 1

    if py > middle_y:
        quadrant += 2
    
    robots_by_quadrant[quadrant] = robots_by_quadrant.get(quadrant, 0) + 1

print(reduce(lambda v, acc: v*acc, robots_by_quadrant.values(), 1))