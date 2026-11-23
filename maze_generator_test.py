import random

width = 6
height = 7
row = 0
col = 0



def is_inside(row, col) -> bool:
    if row >= 0 and row < height and col >= 0 and col < width:
        return True
    else:
        return False

def create_grid(row, col):
    grid[row][col] = 1
    directions = [(0, -1), (0, +1), (-1, 0), (+1, 0)]
    random.shuffle(directions)
    for direction in directions:
        next_row = row + direction[0]
        next_col = col + direction[1]       
        if is_inside(next_row, next_col) is True and grid[next_row][next_col] == 0:
            create_grid(next_row, next_col)
            return
        else:
            continue

if __name__ == "__main__":
    grid = [[0 for colomn in range(width)] for rows in range(height)]
    create_grid(row, col)
    for item in grid:
        for elem in item:
            if elem == 1:
                print("🟩", end=" ")
            elif elem == 0:
                print("⬛", end =" ")
        print()
