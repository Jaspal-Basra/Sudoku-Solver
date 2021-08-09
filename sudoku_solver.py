def check_valid(grid1, t_grid1, row, column, value):
    # Check if the value is valid given the current status of the grid
    if not check_row_valid(grid1, row, value) or not check_column_valid(t_grid1, column, value) or not check_block_valid(grid1, row, column, value):
        return False

    return True


def check_row_valid(grid1, row, value):
    # Check for multiple occurrences of the value in the given row
    if grid1[row].count(value) > 0:
        return False
    return True


def check_column_valid(grid1, col, value):
    # Check for multiple occurrences of the value in the given column
    if grid1[col].count(value) > 0:
        return False
    return True


def check_block_valid(grid1, row, col, value):
    block = []
    block_start = [0, 0]

    # Calculate start of the 3x3 block
    block_start[0] = col - (col % 3)
    block_start[1] = row - (row % 3)

    # Store each value in the 3x3 block into a list
    for i in range(block_start[1], block_start[1] + 3):
        for j in range(block_start[0], block_start[0] + 3):
            block.append(grid1[i][j])

    # Return false for multiple occurrences of the value in the block list
    if block.count(value) > 0:
        return False

    return True


def solve_grid(grid1, t_grid1):
    # Find the next empty space to try
    empty_space = find_next_empty(grid1)

    # If a valid empty space exists, the solution is not finished
    if empty_space:
        # Record the row and column
        row, column = empty_space
    else:
        # Recursion base case (grid is solved)
        return True
    for value_to_try in range(1, 10):
        # Check if the the current value is valid in the selected empty grid position
        if check_valid(grid1, t_grid1, row, column, value_to_try):
            # Update the grid and transposed grid with the valid value
            grid1[row][column] = value_to_try
            t_grid1[column][row] = value_to_try

            # Recursive call to solver
            if solve_grid(grid1, t_grid1):
                return True
            else:
                # Erase current space if solution failed, must backtrack to find another possible solution
                grid1[row][column] = 0
                t_grid1[column][row] = 0
    return False


def find_next_empty(grid1):
    for row in range(len(grid1)):
        for square in range(len(grid1[0])):
            if grid1[row][square] == 0:
                return tuple((row, square))
    return False


def transpose_grid(grid1):
    # Transpose the board so rows become columns and vice-versa
    # This will make it easier to operate on columns

    transposed_grid = []

    for index1 in range(len(grid1[0])):
        row = []
        for index2 in grid1:
            row.append(index2[index1])
        transposed_grid.append(row)

    return transposed_grid


def print_grid(grid1):
    for row in grid1:
        print(row)
    print("\n")


example_grid = [[0, 0, 5, 4, 0, 0, 7, 0, 0], 
                [0, 4, 0, 0, 0, 9, 2, 0, 0], 
                [9, 3, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 9, 0, 0, 0, 0, 3], 
                [0, 0, 2, 8, 0, 0, 0, 0, 6], 
                [6, 0, 3, 0, 0, 5, 0, 0, 1], 
                [0, 0, 4, 0, 1, 0, 0, 0, 2], 
                [0, 0, 6, 5, 0, 0, 8, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Print the grid
print_grid(example_grid)

# Transpose the grid for easy operations for columns
transposed_example_grid = transpose_grid(example_grid)

# Print transposed grid
print_grid(transposed_example_grid)

# Solve the grid
solve_grid(example_grid, transposed_example_grid)

# Print the solved grid
print("Solved grid: ")
print_grid(example_grid)
