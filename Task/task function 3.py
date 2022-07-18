my_list = [[23, 14, 36, 8, 10],
           [12, 15, 56, 32, 0],
           [11, 12, 3, 14, 15],
           [16, 57, 18, 19, 2]]

def total_row_col(my_list, row_A, row_B, col_A, col_B):
    "The function takes on new values and uses them to sum up the newly created rectangle"


    row_A = row_A
    row_B = row_B + 1
    col_A = col_A
    col_B = col_B + 1

    total = 0
    for start in range(row_A, row_B):
        for c_start in range(col_A, col_B):
            total = my_list[start][c_start] +total
    print("Max total is:", total)

total_row_col(my_list, 2, 3, 0, 2)


