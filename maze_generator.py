import random

width = 20
height = 20
perfect = False

class Cell:
    def __init__(self) -> None:
        self.north = True
        self.east = True
        self.south = True
        self.west = True
        self.visited = False
        self.blocked = False


def is_inside(row, col) -> bool:
    if row >= 0 and row < height and col >= 0 and col < width:
        return True
    else:
        return False


def check_neighbors(row: int, col: int, grid: list[list[Cell]]) -> list[tuple[int, int]]:
    neighbors = []
    directions = [(0, -1), (0, +1), (-1, 0), (+1, 0)]
    for direction in directions:
        neighbor_row = row + direction[0]
        neighbor_col = col + direction[1]
        if (
            is_inside(neighbor_row, neighbor_col) 
            and grid[neighbor_row][neighbor_col].visited is False
            and grid[neighbor_row][neighbor_col].blocked is False
        ):
            neighbor_cell = grid[neighbor_row][neighbor_col]
            neighbors.append((neighbor_row, neighbor_col))
    return neighbors


def wall_removal(curr_row: int, curr_col: int, next_row: int,
                 next_col: int, grid: list[list[Cell]]) -> None:
    curr_cell = grid[curr_row][curr_col]
    next_cell = grid[next_row][next_col]
    if next_row < curr_row:
        curr_cell.north = False
        next_cell.south = False
    elif next_row > curr_row:
        curr_cell.south = False
        next_cell.north = False 
    elif next_col < curr_col:
        curr_cell.west = False
        next_cell.east = False
    elif next_col > curr_col:
        curr_cell.east = False
        next_cell.west = False


def create_grid(width: int, height: int) -> list[list[Cell]]:
    grid = [[Cell() for column in range(width)] for rows in range(height)]
    return grid


def maze_generator(width: int, height:int, grid: list[list[Cell]]) -> None:
    active = []
    curr_row = random.randrange(0, height)
    curr_col = random.randrange(0, width)
    active.append((curr_row, curr_col))
    curr_cell = grid[curr_row][curr_col]
    curr_cell.visited = True
    while active != []:
        curr_row, curr_col = active[-1]
        curr_cell = grid[curr_row][curr_col]
        neighbors = check_neighbors(curr_row, curr_col, grid)
        if neighbors == []:
            active.pop()
        else:
            next_row, next_col = random.choice(neighbors)
            next_cell = grid[next_row][next_col]
            wall_removal(curr_row, curr_col, next_row, next_col, grid)
            next_cell.visited = True 
            active.append((next_row, next_col))


def forty_two(grid):
    start_row = int((height - 5) / 2)
    start_col_four = int((width - 7) / 2)
    start_col_two = start_col_four + 4
    start_cell_four = grid[start_row][start_col_four]
    start_cell_four.blocked = True
    start_cell_two = grid[start_row][start_col_two]
    start_cell_two.blocked = True
    for cell in range(2):
        next_row = start_row + 1
        next_cell = grid[next_row][start_col_four]
        next_cell.blocked = True
        start_row = next_row
    for cell in range(2):
        next_col = start_col_four + 1
        next_cell = grid[start_row][next_col]
        next_cell.blocked = True
        start_col_four = next_col
    for cell in range(2):
        next_row = start_row + 1
        next_cell = grid[next_row][start_col_four]
        next_cell.blocked = True        
        start_row = next_row
    start_row = int((height - 5) / 2)
    for cell in range(2):
        next_col = start_col_two + 1
        next_cell = grid[start_row][next_col]
        next_cell.blocked = True
        start_col_two = next_col
    for cell in range(2):
        next_row = start_row + 1
        next_cell = grid[next_row][start_col_two]
        next_cell.blocked = True
        start_row = next_row
    for cell in range(2):
        next_col = start_col_two - 1
        next_cell = grid[start_row][next_col]
        next_cell.blocked = True
        start_col_two = next_col
    for cell in range(2):
        next_row = start_row + 1
        next_cell = grid[next_row][start_col_two]
        next_cell.blocked = True        
        start_row = next_row
    for cell in range(2):
        next_col = start_col_two + 1
        next_cell = grid[start_row][next_col]
        next_cell.blocked = True
        start_col_two = next_col

 

# made by chatgpt, need to redo
def display_maze(grid: list[list[Cell]], width: int, height: int) -> None:
    for row in range(height):
        # Print north walls
        top = ""
        for col in range(width):
            cell = grid[row][col]
            top += "+---" if cell.north else "+   "
        print(top + "+")

        # Print west/east walls
        middle = ""
        for col in range(width):
            cell = grid[row][col]
            middle += "|" if cell.west else " "
            middle += "   "
        middle += "|" if grid[row][width - 1].east else " "
        print(middle)

    # Print bottom walls
    bottom = ""
    for col in range(width):
        cell = grid[height - 1][col]
        bottom += "+---" if cell.south else "+   "
    print(bottom + "+")
 


if __name__ == "__main__":
    grid = create_grid(width, height)
    forty_two(grid)
    maze_generator(width, height, grid)
    display_maze(grid, width, height)
