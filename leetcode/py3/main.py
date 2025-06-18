from src import sudoku
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='Sudoku Solver',
        description='point me at a file with a sudoku grid!')
    parser.add_argument('-f', '--filename')
    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args()

    grid = sudoku.read_grid(args.filename, args.debug)
    sudoku.print_grid(grid, 'Provided grid')
    if sudoku.is_valid_grid(grid, args.debug):
        sudoku.solve_grid(grid, args.debug)
    sudoku.print_grid(grid, 'Solution')


if __name__ == "__main__":
    main()
