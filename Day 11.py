day11_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/11.1.txt", 'r')
content = day11_file.read().split('\n')

# PART 1
# You are given a map of the airport seats which are either --> 'L' empty - '#' occupied - '.' floor --> these alterate simulatanouesly 
# according to the following rule set (note floor spots '.' do not change):
# an empty 'L' seat will be occupied if none of the seats around it are
# an occupied '#' seat will be empty if four or more seats around it are also occupied
# Eventually this map will stabilise --> return the number of occupied seats when this occurs (you are guaranteed stabilisation)

def first_soltuion(seat_layout):
    curr_gen = seat_layout
    rows, cols = len(seat_layout), len(seat_layout[0])
    
    while True:
        next_gen = []

        for x in range(0, rows):
            next_row = ''

            for y in range(0, cols):

                if curr_gen[x][y] == '.':     # continue early to avoid counting neighbours in an unchanging cell
                    next_row += '.'
                    continue              
                
                neighbours = []
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):

                        if (i < 0 or i >= rows) or (j < 0 or j >= cols) or (i, j) == (x, y):
                            continue
                        else:
                            neighbours.append(curr_gen[i][j])   # get the status of all the adjacent neighbours of the current cell

                seated_neighbours = neighbours.count("#")

                if curr_gen[x][y] == 'L':                 
                    next_row += '#' if seated_neighbours == 0 else 'L'
                elif curr_gen[x][y] == '#':
                    next_row += 'L' if seated_neighbours >= 4 else '#'
             
            next_gen.append(next_row)
        
        if (curr_gen == next_gen):
            return ''.join(next_gen).count('#')     # if the previous / current gens match - you have hit a terminal solution
        else:
            curr_gen = next_gen
        
# PART 2
# There are now new rules in how the state of an individual set may change - note a seat's line of sight is blocked by the next seat:
# An empty seat "L" will become occupied if it can see 0 occupied seats in all 8 directions around it
# An occupied seat "#" will become empty if it can see 5 or more occupied seats in all 8 directions around it

def second_solution(seat_layout):
    curr_gen = seat_layout
    rows, cols = len(seat_layout), len(seat_layout[0])
    gen = 0
    while True:
        next_gen = []

        for x in range(0, rows):
            next_row = ''

            for y in range(0, cols):

                if curr_gen[x][y] == '.':
                    next_row += '.'
                    continue
                
                seated_neighbours = 0
                neighbour_steps = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]] # list of neighbours with steps

                for neighbour in neighbour_steps:
                    x_step, y_step, curr_x, curr_y = neighbour[0], neighbour[1], x, y

                    while True:
                        curr_x += x_step
                        curr_y += y_step

                        if (curr_x < 0 or curr_x >= rows or curr_y < 0 or curr_y >= cols):   # handling edge cases
                            break
                        elif curr_gen[curr_x][curr_y] != '.':    # when a non floor spot is reached, check if the seat is occupied

                            if curr_gen[curr_x][curr_y] == '#':   
                                seated_neighbours += 1
                            break

                if curr_gen[x][y] == 'L':                 
                    next_row += '#' if seated_neighbours == 0 else 'L'
                elif curr_gen[x][y] == '#':
                    next_row += 'L' if seated_neighbours >= 5 else '#'

            next_gen.append(next_row)

        if curr_gen == next_gen:
            return ''.join(next_gen).count('#')
        else:
            curr_gen = next_gen
            gen += 1

# tests
print(first_soltuion(content))
print(second_solution(content))
