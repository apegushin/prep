from typing import List, Optional
from datetime import datetime


def read_grid(filename: str, debug: bool) -> Optional[List[List[int]]]:
    grid = []
    with open(filename, 'r') as f:
        if debug: print(f'Successfully opened file {filename} for reading.')
        for l in f.readlines():
            l = l.replace('\n','')
            if debug: print(f'Read line from file: {l} ', end='')
            grid.append([])
            for c in l.split(','):
                match c:
                    case '_':
                        grid[-1].append(0)
                    case _:
                        grid[-1].append(int(c))
            if debug: print(f'and converted to: {grid[-1]}')

    return grid

def print_grid(grid: Optional[List[List[int]]], label: str = ''):
    if grid is None:
        print('The grid is empty! Nothing to print')
        return

    if label != '':
        print(f'{label}:')

    hdiv = '-' * 37
    print(f'{hdiv}')
    for r in grid:
        print('|', end='')
        for c in r:
            print(f' {c} |', end='')
        print(f'\n{hdiv}')

def is_valid_grid(grid: Optional[List[List[int]]], debug: bool):
    return True

def solve_grid(grid: Optional[List[List[int]]], debug: bool):
    if grid is None:
        print('The grid is empty! Nothing to solve')
        return

    def sqr_set_idx(i: int, j: int) -> int:
        return 3*(i // 3) + j // 3

    rows_sets = [set() for _ in range(9)]
    cols_sets = [set() for _ in range(9)]
    sqrs_sets = [set() for _ in range(9)]
    if debug: print('Received a grid and initialized sets for rows, columns and smaller squares')

    for i in range(9):
        for j in range(9):
            c = grid[i][j]
            if grid[i][j] != 0:
                rows_sets[i].add(c)
                cols_sets[j].add(c)
                sqrs_sets[sqr_set_idx(i, j)].add(c)
    if debug:
        print(f'Rows sets for provided grid: {rows_sets =}')
        print(f'Columns sets for provided grid: {cols_sets = }')
        print(f'Squares sets for provided grid: {sqrs_sets = }')

    ts_start = datetime.now()
    if debug:
        print(f'Starting to solve the grid at {ts_start.ctime()}')

    def dfs_solver(i_s, j_s) -> bool:
        i, j = i_s, j_s
        while i < 9:
            while j < 9:
                if grid[i][j] == 0:
                    for cand in range(1, 10):
                        if (cand not in rows_sets[i]
                                and cand not in cols_sets[j]
                                and cand not in sqrs_sets[sqr_set_idx(i, j)]):
                            grid[i][j] = cand
                            rows_sets[i].add(cand)
                            cols_sets[j].add(cand)
                            sqrs_sets[sqr_set_idx(i, j)].add(cand)
                            if dfs_solver(i, j):
                                return True
                            grid[i][j] = 0
                            rows_sets[i].remove(cand)
                            cols_sets[j].remove(cand)
                            sqrs_sets[sqr_set_idx(i, j)].remove(cand)
                    return False
                j += 1
            j = 0
            i += 1
        return True

    dfs_solver(0, 0)




























