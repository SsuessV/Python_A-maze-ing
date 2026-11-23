import random

width = 6
height = 7

class Cell:
    def __init__(self) -> None:
        self.north = True
        self.east = True
        self.south = True
        self.west = True
        self.visited = False

    def direction(self) -> tuple[int, int]:
        directions = [(0, -1), (0, +1), (-1, 0), (+1, 0)]
        chosen = random.choice(directions)
        return chosen


def create_grid(width: int, height: int) -> list[list[Cell]]:
    grid = [[Cell() for column in range(width)] for rows in range(height)]
    return grid


def growing_tree(grid):
    active = []
    curr_cell = grid[0][0]
    curr_cell.visited = True
    active.append(curr_cell)
    for cell in active:
        row, col = curr_cell.direction()
        


if __name__ == "__main__":
    grid = create_grid(width, height)
    print_grid(grid)
