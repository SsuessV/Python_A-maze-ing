import random

width = 5
height = 5
perfect = False
entry = (0, 1)
exit_point = (16, 4)

class Cell:
    def __init__(self) -> None:
        self.north = True
        self.east = True
        self.south = True
        self.west = True
        self.visited = False
        self.blocked = False
        #self.path = False

    def hex_output(self) -> str:
        value_north = 1
        value_east = 2
        value_south = 4
        value_west = 8
        total_value = 0
        if self.north is True:
            total_value += value_north
        if self.east is True:
            total_value += value_east
        if self.south is True:
            total_value += value_south
        if self.west is True:
            total_value += value_west
        return format(total_value, "X")
    


def is_inside(width, height, row, col) -> bool:
    if row >= 0 and row < height and col >= 0 and col < width:
        return True
    else:
        return False


def check_neighbors(width:int, height: int, row: int, 
                    col: int, grid: list[list[Cell]]) -> list[tuple[int, int]]:
    neighbors = []
    directions = [(0, -1), (0, +1), (-1, 0), (+1, 0)]
    for direction in directions:
        neighbor_row = row + direction[0]
        neighbor_col = col + direction[1]
        if (
            is_inside(width, height, neighbor_row, neighbor_col) 
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
        neighbors = check_neighbors(width, height, curr_row, curr_col, grid)
        if neighbors == []:
            active.pop()
        else:
            next_row, next_col = random.choice(neighbors)
            next_cell = grid[next_row][next_col]
            wall_removal(curr_row, curr_col, next_row, next_col, grid)
            next_cell.visited = True 
            active.append((next_row, next_col))


def forty_two(grid: list[list[Cell]]) -> None:
    if height < 9 or width < 9:
        print("[WARNING] The given dimensions are too small "
              "to add the number '42' in the middle of the maze.")
        return
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
    start_row = int((height - 5) / 2)
    start_col_four = int((width - 7) / 2) + 2
    start_cell_four = grid[start_row][start_col_four]
    start_cell_four.blocked = True
    for cell in range(4):
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


def imperfect_maze(width: int, height: int, grid: list[list[Cell]]) -> None:
    curr_row, curr_col = (0, 0)
    for row in grid:
        for cell in row:
            curr_cell = grid[curr_row][curr_col]
            next_col = curr_col + 1
            if is_inside(width, height, curr_row, next_col) is True:
                next_cell = grid[curr_row][next_col]
            else: 
                break
            if (next_cell.blocked is False 
                and curr_cell.blocked is False 
                and curr_cell.east is True
            ):
                if random.random() < 0.30:
                    wall_removal(curr_row, curr_col, curr_row, next_col, grid)
            curr_col = next_col
        curr_row += 1
        curr_col = 0
    curr_row, curr_col = (0, 0)
    for _ in range(width):
        for _ in range(height):
            curr_cell = grid[curr_row][curr_col]
            next_row = curr_row + 1
            if is_inside(width, height, next_row, curr_col) is True:
                next_cell = grid[next_row][curr_col]
            else: 
                break
            if (next_cell.blocked is False 
                and curr_cell.blocked is False 
                and curr_cell.south is True
            ):
                if random.random() < 0.30:
                    wall_removal(curr_row, curr_col, next_row, curr_col, grid)
            curr_row = next_row
        curr_col += 1
        curr_row = 0
       
def create_output(entry, exit_point, grid):
    hexa_list = []
    for row in grid:
        hex_value = ""
        for cell in row:
            hex_value += cell.hex_output()
        hex_value += "\n"
        hexa_list.append(hex_value)
    with open("maze.txt", "w") as file:
        file.writelines(hexa_list)
        file.write("\n")
        file.write(str(entry))
        file.write("\n")
        file.write(str(exit_point))
        

"""
def find_path(grid: list[list[Cell]], entry: tuple[int, int],
              exit_point: tuple[int, int]) -> dict:
    for row in grid:
        for cell in row:
            cell.visited = False
    queue = []
    curr_row,curr_col = entry
    curr_cell = grid[curr_row][curr_col]
    curr_cell.visited = True
    queue.append(entry)
    previous = {}
    while queue != []:
        curr_row,curr_col = queue[0]
        if (curr_row, curr_col) == exit_point:
            break
        queue.pop(0)
        neighbors = check_neighbors(curr_row, curr_col, grid)
        for neighbor in neighbors:
            next_row, next_col = neighbor
            next_cell = grid[next_row][next_col]
            if next_cell.visited is False:
                next_cell.visited = True
                queue.append((next_row, next_col))
                previous.update({(next_row, next_col): (curr_row, curr_col)})
    return previous

        
def final_path(path_coords: dict, entry, exit_pointi, grid) -> list:
    path = []
    curr_cell = exit_point
    while curr_cell != entry:
        path.append(curr_cell)
        curr_row, curr_col = curr_cell
        cell = grid[curr_row][curr_col]
        cell.path = True
        curr_cell = path_coords[curr_cell]
    path.append(entry)
    path.reverse()
    return path
"""

#made by chatgpt for visualization
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
            middle += "###" if cell.blocked else "   "

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
    if perfect is False:
        imperfect_maze(width, height, grid)
    display_maze(grid, width, height)
    create_output(entry, exit_point, grid)

