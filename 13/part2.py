import sys
import re
from functools import lru_cache
from math import floor, ceil

A_COST = 3
B_COST = 1
INF = 1 << 60
ADJUSTMENT = 10000000000000

def getMachineInfo(data):
    ax, ay, bx, by, tx, ty = map(int, re.findall(r"\d+", data))

    return (ax, ay), (bx, by), (tx + ADJUSTMENT, ty + ADJUSTMENT)

def mcd(a, b):
    if a == 1 or b == 1:
        return 1

def solve(a, b, t):
    ax, ay = a
    bx, by = b
    tx, ty = t

    # find integer solutions for
    # ax*p + bx*q = tx
    # ay*p + by*q = ty

    if by * ax != bx * ay:  # unique solution
        q = (ty*ax - tx*ay)//(by*ax - bx*ay)
        p = (tx - q * bx) // ax

        if p < 0 or q < 0:
            return INF

        # the solution can be non integer, if so p and q 
        # computed using integer division "//" are not solutions
        if ax*p + bx*q != tx  or ay*p + by*q != ty:
            return INF

        return 3 * p + q

    if ty * ax != tx * ay:  # if linear independent (no solutions)
        return INF
    

    # multiple solutions

    _mcd = mcd(ax, bx)
    if tx % _mcd != 0: # no integer solutions
        return INF
    
    # simplified equation params
    _ax, _bx, _tx = ax//_mcd, bx//_mcd, tx//_mcd
    
    found = False
    # try to find on integer solution
    for _p in range(_bx):
        # q = (tx - p*ax)/bx
        if (_tx - p*_ax)%_bx == 0:
            found = True
            _q = (_tx - p*_ax)//_bx
            break
    
    if not found:
        return INF
    
    # all integer solutions are of the form
    # p = _p + _bx*k
    # q = _q - _ax*k

    # we want to minimize 3*p + q, with p and q non negative integers
    # is the same to minimize 3*(_p + _bx*k) + _q - _ax*k => k*(3*bx - ax) + 3*_p + _q
    # with 2 restrictions:
    # p >= 0 => _p + _bx*k >= 0  => _bx*k >= -_p => k >= -_p/bx if _bx > 0 else k <= -_p/bx
    # q >= 0 => _q - _ax*k >= 0  => _ax*k <= _q => k <= _q/ax if _ax > 0 else k <= _q/ax

    min_k = -INF
    max_k = INF

    if _bx > 0:
        min_k = -ceil(_p/bx)
    else:
        max_k = -floor(_p/bx)

    if _ax > 0:
        max_k = min(ceil(_q/ax), min_k)
    else:
        min_k = max(floor(_q/ax), max_k)

    k = min_k if 3*_bx - _ax > 0 else max_k

    p = _p + _bx*k
    q = _q - _ax*k

    return 3*p + q

machines = [getMachineInfo(data) for data in open(sys.argv[1]).read().strip().split("\n\n")]
total = 0

for i, (a, b, t) in enumerate(machines):
    tokens = solve(a, b, t)
    if tokens < INF:
        total += tokens

print(total)