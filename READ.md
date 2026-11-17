*This project has been created as part of the 42 curriculum by suyoun and bsurilla.*

# A-Maze-ing

## Description

**A-Maze-ing** is a maze generation project from the 42 curriculum, completed as a two-person group project.

The objective is to generate a maze based on user-defined configuration parameters, find the shortest path between the entry and exit, and export the resulting maze into a specified output file.

The program reads and validates a configuration file containing the maze dimensions, entry and exit coordinates, output filename, and generation mode.

The project focuses on algorithm design, object-oriented programming, file parsing, graph traversal, pathfinding, and hexadecimal encoding.

## Contributors

This project was developed by:

- Drucilla Tricia Calore (drcalore) its just what ai generated so edit the list as u go
  - Implemented configuration file parsing and validation.
  - Designed the `Cell` class and maze data representation.
  - Implemented the two-dimensional grid initialization.
  - Developed maze generation logic and cell connectivity.
  - Implemented hexadecimal encoding and maze output generation.
  - Wrote README documentation with the help of AI.
  - Performed testing, debugging, and integration.

- Su Jung Youn (suyoun)
  - Implemented [responsibility].
  - Developed [responsibility].
  - Implemented [responsibility].
  - Worked on maze visualization and user interaction.
  - Performed testing, debugging, and integration.
  - Designed the `Cell` class and maze data representation.
  - Implemented the two-dimensional grid initialization.
  - Developed maze generation logic and cell connectivity.
  - Implemented hexadecimal encoding and maze output generation.
  - Wrote README documentation with the help of AI.
  - Performed testing, debugging, and integration.

---

## Instructions

### Compilation

To install the required dependencies, run:

```bash
make install
```

To run the project:

```bash
make run
```

To run code quality checks:

```bash
make lint
```

To remove temporary files and Python caches:

```bash
make clean
```

### Usage

Run the maze generator by providing a configuration file:

```bash
python3 a_maze_ing.py config.txt
```

The program reads the configuration file, validates the parameters, generates the maze, calculates the shortest path, and writes the resulting maze to the specified output file.

### Configuration File

The configuration file defines the parameters used for maze generation.

Each parameter follows the format:

```text
KEY=VALUE
```

Example:

```text
# Maze dimensions
WIDTH=10
HEIGHT=8

# Entry and exit coordinates
ENTRY=0,0
EXIT=9,7

# Output filename
OUTPUT_FILE=maze.txt

# Generation mode
PERFECT=True
```

The configuration parameters are:

| Parameter | Description | Example |
|---|---|---|
| WIDTH | Number of columns in the maze | 10 |
| HEIGHT | Number of rows in the maze | 8 |
| ENTRY | Starting coordinates | 0,0 |
| EXIT | Ending coordinates | 9,7 |
| OUTPUT_FILE | Name of the output file | maze.txt |
| PERFECT | Determines whether the maze is perfect | True |

The parser reads the configuration file and converts the values into the appropriate Python data types.

For example:
- `WIDTH` and `HEIGHT` are converted into integers.
- `ENTRY` and `EXIT` are converted into coordinate tuples.
- `PERFECT` is converted into a boolean.

The parser also validates the configuration to ensure that the required parameters are present and that the provided values are valid.

### Maze Output

The generated maze is saved to the output file.

Each cell is represented by a hexadecimal character encoding the state of its four walls.

The output also contains:
- The hexadecimal representation of the maze.
- The entry coordinates.
- The exit coordinates.
- The shortest path represented using directional characters.

---

## Resources

### References

- 42 A-Maze-ing project subject and evaluation guidelines.
- Python official documentation: https://docs.python.org/3/
- Python documentation on classes and objects: https://docs.python.org/3/tutorial/classes.html
- Python documentation on file handling: https://docs.python.org/3/tutorial/inputoutput.html
- Python documentation on random numbers: https://docs.python.org/3/library/random.html
- Python documentation on `collections.deque`: https://docs.python.org/3/library/collections.html
- Tutorials and explanations about Depth-First Search (DFS), Breadth-First Search (BFS), and maze generation algorithms.
- Assistance and discussions with other 42 students.

### AI Usage

AI tools such as ChatGPT were used as learning and review aids during the development of this project.

They were used to:
- Explain Python concepts, including classes, objects, lists, and file handling.
- Clarify configuration parsing and input validation.
- Discuss maze generation algorithms and cell connectivity.
- Explain graph traversal and shortest path algorithms.
- Understand hexadecimal representation and bitwise operations.
- Review implementation approaches and help identify potential edge cases.
- Assist with debugging and understanding error messages.
- Help structure and refine the project documentation (README).

All AI-generated suggestions were reviewed and adapted by the authors. The final implementation was tested and validated by the team.

---

## Algorithm and Data Structure Choices

### Maze Generation Algorithms

We are implementing two maze generation algorithms: **Growing Tree** and **Randomized Prim's**.

#### 1. Growing Tree Algorithm

The Growing Tree algorithm generates a maze by maintaining a list of active cells.

1. Start with the entry cell and mark it as visited.
2. Add the entry cell to the active list.
3. Select a cell from the active list.
4. Find its unvisited neighboring cells.
5. If unvisited neighbors exist, randomly select one.
6. Open the wall between the current cell and the selected neighbor.
7. Mark the selected cell as visited and add it to the active list.
8. If no unvisited neighbors exist, remove the current cell from the active list.
9. Repeat until the active list is empty.

The way cells are selected from the active list influences the structure of the generated maze.

#### 2. Randomized Prim's Algorithm**

Randomized Prim's algorithm generates a maze using a frontier list containing unvisited cells adjacent to the visited area.

1. Start with the entry cell and mark it as visited.
2. Add its unvisited neighbors to the frontier list.
3. Randomly select a cell from the frontier list.
4. Find its already visited neighbors.
5. Randomly choose one of those visited neighbors.
6. Open the wall between the selected cell and the chosen neighbor.
7. Mark the selected cell as visited.
8. Add its unvisited neighbors to the frontier list.
9. Repeat until the frontier list is empty.

This algorithm expands the maze from the visited area by connecting frontier cells to already visited cells.

### Perfect and Non-Perfect Mazes

A **perfect maze** is a maze in which:
- Every cell is reachable.
- There is exactly one possible path between any two cells.
- No loops exist.

A **non-perfect maze** allows additional connections between cells, creating loops and alternative routes.

The `PERFECT` configuration parameter determines which type of maze is generated.

### Shortest Path Algorithm

**Breadth-First Search (BFS)**

BFS is used to find the shortest path between the entry and exit cells.

Because every movement between neighbouring cells has the same cost, BFS guarantees the shortest path in terms of the number of cell transitions.

The algorithm:
1. Starts at the entry cell.
2. Explores all accessible neighbouring cells.
3. Uses a queue to process cells in the order they are discovered.
4. Records the predecessor of each visited cell.
5. Stops when the exit is reached.
6. Reconstructs the shortest path by following the recorded predecessors.

### Data Structures

**Two-dimensional list**

A nested list is used to represent the maze grid.

The outer list represents rows, while each inner list contains the cells belonging to that row.

This structure allows cells to be accessed using their coordinates:

```python
maze[y][x]
```

**Cell class**

A `Cell` class represents an individual maze cell.

Each instance stores the state of its four walls and its visitation status.

Using a class allows each cell to maintain its own independent state and makes the maze easier to manage.

**Active List**

The Growing Tree algorithm uses an active list to keep track of cells that can still be expanded.

**Frontier List**

Randomized Prim's algorithm uses a frontier list to store unvisited cells adjacent to the visited area.

**Queue**

A queue is used during BFS to process cells in first-in, first-out order.

This ensures that cells are explored level by level when searching for the shortest path.

**Hexadecimal representation**

Each cell's four wall states are encoded into four bits.

The resulting binary value is converted into a hexadecimal character.

Four bits provide 16 possible combinations, meaning one hexadecimal character is sufficient to represent all possible wall configurations of a cell.

---

## Notes

This project focuses on:

- Designing and implementing maze generation algorithms.
- Understanding object-oriented programming through classes and objects.
- Representing a maze using a two-dimensional data structure.
- Parsing and validating configuration files.
- Understanding graph traversal using DFS and BFS.
- Implementing backtracking to generate connected mazes.
- Finding the shortest path between two coordinates.
- Understanding binary and hexadecimal representations.
- Using bitwise operations to encode wall information.
- Reading from and writing to files.
- Working collaboratively using Git and GitHub.
- Testing, debugging, and integrating different components of a group project.

---

## License

This project was developed as part of the 42 curriculum.