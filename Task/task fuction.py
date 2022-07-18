def sum_column_row(my_list):
    """A function that summarizes the rows and columns in the list, each one individually.
    The function returns as an answer the index number that the sum of the members in the same row is the highest,
    and returns separately the number of the column with the highest amount."""


    sum_row = 0
    index = -1
    max_index = 0

    for i in my_list:
        index = index + 1
        if sum(i) > sum_row:
            sum_row = sum(i)
            max_index = index


    column_max = 0
    sum1 = 0
    column_index = -1

    for L in range(0, len(my_list[0])):
        for j in range(0, len(my_list)):
            if L == L:
                sum1 = sum1 + my_list[j][L]
        if sum1 > column_max:
            column_max = sum1
            column_index = L
        sum1 = 0
    result = ("max column", column_index, "max row", max_index)
    return result

my_list = [[23, 14, 36, 8, 10],
           [12, 15, 56, 32, 0],
           [11, 12, 3, 14, 15],
           [16, 57, 18, 19, 2]]

print(sum_column_row(my_list))