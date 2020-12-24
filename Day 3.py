day3_file = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/Input Files/3.1.txt", 'r')

# Put the rows into a 2D matrix
raw_text = day3_file.read()
grid = [row for row in raw_text.split('\n')] 

# PART 1
# works through the grid start at the top left position moving right 3, then down 1 - the grid extends infinitely to the right repeating the 
# pattern in the raw-text dump
# reports the number of trees 'X' which will be landed on as the grid is traversed

def first_solution(input_grid, right_steps, down_steps):
    total = 0
    num_rows = len(input_grid)
    row_length = len(input_grid[0])

    row, col = 0, 0

    while row < num_rows - down_steps:
        row += down_steps
        col += right_steps

        if input_grid[row][col % row_length] == '#':
            total += 1

    return total

# PART 2
# now find the product of the total number of trees one might encounter for the following movement patterns:
# R1 D1 - R3 D1 - R5 D1 - R7 D1 - R1 D2 --> Right Down

# tests
print(first_solution(grid, 3, 1))  # this is part 1
print(first_solution(grid, 1, 1) * first_solution(grid, 3, 1) * 
      first_solution(grid, 5, 1) * first_solution(grid, 7, 1) * first_solution(grid, 1, 2))
