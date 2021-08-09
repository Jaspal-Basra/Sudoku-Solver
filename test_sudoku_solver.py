import sudoku_solver


def run_tests():
    ret_val = True

    print("Running tests...")

    if not test_find_next_empty():
        print("test_find_next_empty failed")
        ret_val = False

    if not test_transpose_grid():
        print("test_transpose_grid failed")
        ret_val = False

    if not test_check_valid():
        print("test_check_valid failed")
        ret_val = False

    if not test_solved_grid():
        print("test_solved_grid failed")
        ret_val = False

    return ret_val


def test_solved_grid():
    # Test for solve_grid function
    ret_val = True

    grid1 = [[0, 0, 5, 4, 0, 0, 7, 0, 0], 
             [0, 4, 0, 0, 0, 9, 2, 0, 0], 
             [9, 3, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 9, 0, 0, 0, 0, 3], 
             [0, 0, 2, 8, 0, 0, 0, 0, 6], 
             [6, 0, 3, 0, 0, 5, 0, 0, 1], 
             [0, 0, 4, 0, 1, 0, 0, 0, 2], 
             [0, 0, 6, 5, 0, 0, 8, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    transposed_grid1 = sudoku_solver.transpose_grid(grid1)
    sudoku_solver.solve_grid(grid1, transposed_grid1)

    # This grid contains exactly one error in each row, column, and 3x3 block (for negative testing)
    grid2 = [[1, 6, 5, 4, 8, 3, 7, 1, 9],
             [1, 4, 7, 7, 5, 9, 2, 3, 8],
             [9, 3, 8, 1, 2, 7, 9, 5, 4],
             [8, 3, 1, 9, 6, 4, 5, 2, 3],
             [4, 5, 2, 8, 4, 1, 9, 7, 6],
             [6, 9, 3, 2, 7, 5, 4, 5, 1],
             [5, 8, 2, 7, 1, 6, 3, 9, 2],
             [3, 1, 6, 5, 9, 8, 8, 4, 7],
             [7, 2, 9, 3, 4, 8, 1, 6, 6]]

    transposed_grid2 = sudoku_solver.transpose_grid(grid2)
    sudoku_solver.solve_grid(grid2, transposed_grid2)

    # The values that repeat in each row, column, and block respectively for grid 2
    row_values_repeating = [1, 7, 9, 3, 4, 5, 2, 8, 6]
    col_values_repeating = [1, 3, 2, 7, 4, 8, 9, 5, 6]
    block_values_repeating = [1, 7, 9, 3, 4, 5, 2, 8, 6]

    # Check that occurrence of every possible number in each row is 1
    for row in range(len(grid1)):
        for test_val in range(1, 10):
            cnt = grid1[row].count(test_val)
            if cnt != 1:
                print("ERROR: test_solved_grid: Value " + str(test_val) + " appears in row " + str(row + 1) + " " + str(cnt) + " times.")
                ret_val = False

    column_buf = []

    # Check that occurrence of every possible number in each row is 1
    for col in range(len(grid1[0])):
        for row in range(len(grid1)):
            column_buf.append(grid1[row][col])
        for test_val in range(1, 10):
            cnt = column_buf.count(test_val)
            if cnt != 1:
                print("ERROR: test_solved_grid: Value " + str(test_val) + " appears in column " + str(col + 1) + " " + str(cnt) + " times.")
                ret_val = False
        column_buf.clear()

    for block in range(1, 10):
        if not test_block_solved(grid1, block, False, block_values_repeating):
            ret_val = False

    # Check that occurrence of every possible number in each row is 1
    for row in range(len(grid2)):
        cnt = grid2[row].count(row_values_repeating[row])
        if cnt != 2:
            print("ERROR: test_solved_grid: Value " + str(test_val) + " appears in row " + str(row + 1) + " " + str(cnt) + " time.")
            ret_val = False

    column_buf.clear()
    
    # Check that occurrence of every possible number in each row is not 1
    for col in range(len(grid2[0])):
        for row in range(len(grid2)):
            column_buf.append(grid2[row][col])
        cnt = column_buf.count(col_values_repeating[col])
        if cnt != 2:
            print("ERROR: test_solved_grid: Value " + str(test_val) + " appears in column " + str(col + 1) + " " + str(cnt) + " time.")
            ret_val = False
        column_buf.clear()
    
    for block in range(1, 10):
        if not test_block_solved(grid2, block, True, block_values_repeating):
            ret_val = False

    return ret_val


def test_block_solved(grid1, block_num, neg, block_vals_repeating):
    ret_val = True
    block_buf = []
    lower_limit_col = ((block_num - 1) % 3) * 3
    lower_limit_row = ((block_num - 1) // 3) * 3

    for row in range(lower_limit_row, lower_limit_row + 3):
        for col in range(lower_limit_col, lower_limit_col + 3):
            block_buf.append(grid1[row][col])
    if neg:
        cnt = block_buf.count(block_vals_repeating[block_num - 1])
        if cnt != 2:
            print("ERROR: test_solved_grid: Value " + str(block_vals_repeating[block_num - 1]) + " appears in block " + str(block_num) + " " + str(cnt) + " time.")
            ret_val = False
    else:
        for test_val in range(1, 10):
            cnt = block_buf.count(test_val)
            if cnt != 1:
                print("ERROR: test_solved_grid: Value " + str(test_val) + " appears in block " + str(block_num) + " " + str(cnt) + " times.")
                ret_val = False
        

    return ret_val


def test_check_valid():
    # Test for check_valid function
    ret_val = True
    grid1 = [[2, 6, 5, 4, 8, 3, 7, 1, 9], 
             [1, 4, 7, 6, 5, 9, 2, 3, 8], 
             [9, 3, 8, 1, 2, 7, 6, 5, 4],
             [8, 7, 1, 9, 6, 4, 5, 2, 3], 
             [4, 5, 2, 8, 3, 1, 9, 7, 6], 
             [6, 9, 3, 2, 7, 5, 4, 8, 1],
             [5, 8, 4, 7, 1, 6, 3, 9, 2], 
             [3, 1, 6, 5, 9, 2, 8, 4, 7], 
             [7, 2, 9, 3, 4, 8, 1, 6, 5]]

    t_grid1 = sudoku_solver.transpose_grid(grid1)

    for row in range(len(grid1)):
        for col in range(len(grid1[0])):
            for i in range(1, 10):
                if sudoku_solver.check_valid(grid1, t_grid1, row, col, i):
                    print("ERROR: test_check_valid: Valid space found at row: " + str(row + 1) + " and column: " + str(col + 1) + " for value: " + str(i))
                    ret_val = False

    for row in range(len(grid1)):
        for col in range(len(grid1[0])):
            val_backup = grid1[row][col]
            grid1[row][col] = 0
            t_grid1[col][row] = 0
            if not sudoku_solver.check_valid(grid1, t_grid1, row, col, val_backup):
                print("ERROR: test_check_valid: Valid space not found at row: " + str(row + 1) + " and column: " + str(col + 1) + " for value: " + str(val_backup))
                ret_val = False
            grid1[row][col] = val_backup
            t_grid1[col][row] = val_backup

    return ret_val


def test_transpose_grid():
    # Test for transpose_grid function
    ret_val = True
    grid1 = [[2, 6, 5, 4, 8, 3, 7, 1, 9],
             [1, 4, 7, 6, 5, 9, 2, 3, 8],
             [9, 3, 8, 1, 2, 7, 6, 5, 4],
             [8, 7, 1, 9, 6, 4, 5, 2, 3],
             [4, 5, 2, 8, 3, 1, 9, 7, 6],
             [6, 9, 3, 2, 7, 5, 4, 8, 1],
             [5, 8, 4, 7, 1, 6, 3, 9, 2],
             [3, 1, 6, 5, 9, 2, 8, 4, 7],
             [7, 2, 9, 3, 4, 8, 1, 6, 5]]

    t_grid1 = sudoku_solver.transpose_grid(grid1)

    # Compare the grid and the transposed grid to ensure it was transposed correctly
    for row in range(len(grid1)):
        for col in range(len(grid1[0])):
            if grid1[row][col] != t_grid1[col][row]:
                print("ERROR: test_transpose_grid: Grid was not transposed correctly.")
                ret_val = False

    return ret_val


def test_find_next_empty():
    # Test for find_next_empty function
    ret_val = True
    grid1 = [[2, 6, 5, 4, 8, 3, 7, 1, 9],
             [1, 4, 7, 6, 5, 9, 2, 3, 8],
             [9, 3, 8, 1, 2, 7, 6, 5, 4],
             [8, 7, 1, 9, 6, 4, 5, 2, 3],
             [4, 5, 2, 8, 3, 1, 9, 7, 6],
             [6, 9, 3, 2, 7, 5, 4, 8, 1],
             [5, 8, 4, 7, 1, 6, 3, 9, 2],
             [3, 1, 6, 5, 9, 2, 8, 4, 7],
             [7, 2, 9, 3, 4, 8, 1, 6, 5]]

    pos = sudoku_solver.find_next_empty(grid1)

    for row in range(len(grid1)):
        for col in range(len(grid1[0])):
            val_backup = grid1[row][col]
            grid1[row][col] = 0
            if sudoku_solver.find_next_empty(grid1) != (row, col):
                print("ERROR: test_find_next_empty: Empty space not found at row " + str(row + 1) + " and column " + str(col + 1))
                ret_val = False
            grid1[row][col] = val_backup

    return ret_val


# Run test to ensure grid was solved correctly
if run_tests():
    print("Sudoku solver tests passed!")
else:
    print("Sudoku solver tests failed.")
