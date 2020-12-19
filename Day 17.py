import numpy as np

day17_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/17.1.txt", 'r')
cube_array = [[list(line) for line in day17_file.read().split('\n')]]
array_ht, array_wdth, array_dpth, array_4D = len(cube_array[0]), len(cube_array[0][0]), 1, 1  # get the base size of the grid (8x8x1x1)

# code to initialise the base grid
def initialise_grid(is4D):
    if not is4D:
        active_grid = np.full((array_dpth, array_wdth, array_ht), cube_array)  # create the n-dimensional grid to store the cube array
        active_grid = np.pad(active_grid, 2, constant_values='.')  # add padding to avoid index errors and ease in value checking 
    else:
        active_grid = np.full((array_4D, array_dpth, array_wdth, array_ht), cube_array)
        active_grid = np.pad(active_grid, 2, constant_values='.')

    return active_grid

# PART 1
# You are given a starting slice of an infinite 3D space consisting of Conway Cubes which can either be active ('#') or inactive('.')
# After a cycle all the cubes which could *potentially* change state may become active or inactive depending on the following rules:
# If active --> if 2-3 neighbours are also active --> the cube remains active, otherwise the cube becomes inactive
# If inactive --> if 3 neighbours are active --> the cube becomes active, otherwise the cube remains inactive
# Each cube has an (x, y, z) coorindate associated with it's space relative to the initial slice - find the total active cubes after 6 cycles

def active_neighbours(active_grid, coord, trackNeighbours, is4D):
    neighbours, num_active = [], 0
    z, y, x = coord[0], coord[1], coord[2]
    
    if is4D:
        w = coord[3]
        for k in range(z-1, z+2):
            for j in range(y-1, y+2):
                for i in range(x-1, x+2):
                    for h in range(w-1, w+2):
                        if h==w and i==x and j==y and k==z:
                            continue
                        else:
                            num_active += 1 if active_grid[k][j][i][h] == '#' else 0
                            if trackNeighbours:
                                neighbours.append([k, j, i, h])
        return neighbours, num_active

    else:
        for k in range(z-1, z+2):
            for j in range(y-1, y+2):
                for i in range(x-1, x+2):
                    if i==x and j==y and k==z:
                        continue
                    else:
                        num_active += 1 if active_grid[k][j][i] == '#' else 0
                        if trackNeighbours:
                            neighbours.append([k, j, i])
        return neighbours, num_active

def first_solution(cycles, is4D):
    curr_gen = initialise_grid(is4D)

    for i in range(cycles):
        z, y, x = np.where(curr_gen == '#')  # get the coordinates of every active cube in the current generation
        active_cubes = list(zip(z, y, x))
        next_gen = curr_gen.copy()  # initialise the next grid to store the activity changes

        for cube_coord in active_cubes:
            neighbours, total_active = active_neighbours(curr_gen, cube_coord, True, False)
            z, y, x = cube_coord[0], cube_coord[1], cube_coord[2]

            if not(2 <= total_active <= 3):   # if active cube has 2/3 neighbours - it stays alive, else inactive
                next_gen[z][y][x] = '.'

            for neighbour in neighbours:
                z, y, x = neighbour[0], neighbour[1], neighbour[2]
                if curr_gen[z][y][x] == '#':
                    continue
                else:
                    total_active = active_neighbours(curr_gen, neighbour, False, False)[1]
                    if total_active == 3:
                        next_gen[z][y][x] = '#'

        curr_gen = np.pad(next_gen, 1, constant_values='.')  # expand the grid to account for new edge cases
  
    return (curr_gen == '#').sum()  # return the total number of active cubes in the array


# PART 2
# Same as part 1, except now the grid has a 4th dimension! Still perform 6 cycles and return the total number of active cubes

def second_solution(cycles, is4D):
    curr_gen = initialise_grid(is4D)

    for i in range(cycles):
        z, y, x, w = np.where(curr_gen == '#')  # get the coordinates of every active cube in the current generation
        active_cubes = list(zip(z, y, x, w))
        next_gen = curr_gen.copy()  # initialise the next grid to store the activity changes

        for cube_coord in active_cubes:
            neighbours, total_active = active_neighbours(curr_gen, cube_coord, True, True)
            z, y, x, w = cube_coord[0], cube_coord[1], cube_coord[2], cube_coord[3]

            if not (2 <= total_active <= 3):   # if active cube has 2/3 neighbours - it stays alive, else inactive
                next_gen[z][y][x][w] = '.'

            for neighbour in neighbours:
                z, y, x, w = neighbour[0], neighbour[1], neighbour[2], neighbour[3]
                if curr_gen[z][y][x][w] == '#':
                    continue
                else:
                    total_active = active_neighbours(curr_gen, neighbour, False, True)[1]
                    if total_active == 3:
                        next_gen[z][y][x][w] = '#'

        curr_gen = np.pad(next_gen, 1, constant_values='.')  # expand the grid to account for new edge cases
  
    return (curr_gen == '#').sum()  # return the total number of active cubes in the array

# tests
print(first_solution(6, False))
print(second_solution(6, True))
