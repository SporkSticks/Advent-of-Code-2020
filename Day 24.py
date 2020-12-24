day24_file = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/Input Files/24.1.txt", 'r')
tiles = day24_file.read().split('\n')

# PART 1
# You have to build up a hexagonal grid of floor tiles - your input is a list of directions to find a particular tile
# All tiles start white, when you land on a tile, you flip it over - you start at a centre tile (0,0) in an infinite grid
# Tiles have 6 neighbours --> w/e/nw/ne/sw/se --> tiles are oriented to point upwards
# After all the instructions are followed, how many tiles are black

def first_solution(tiles, p2=False):
    visited_tiles = {}  # store tiles in the form - {(x, y): 'colour', ...} - colour is initially white - flips when visited
    movements = {'w': (-1, 0), 'e': (1, 0), 'nw': (0, 1), 'sw': (-1, -1), 'ne': (1, 1), 'se': (0, -1)}

    for tile in tiles:
        x, y = 0, 0

        tmp = ''
        for char in tile:       
            if tmp:  # if there is a temporary character waiting - it is part of a two char movement
                tmp += char
                x += movements[tmp][0]
                y += movements[tmp][1]
                tmp = ''

            else:
                if char in 'ew':  # the movement is one char long, apply it and move to the next direction                
                    x += movements[char][0]
                    y += movements[char][1]
                else:
                    tmp += char  # if the character is not e/w it is n/s and needs the following character
     
        if (x, y) in visited_tiles.keys():
            visited_tiles[(x, y)] = 'black' if visited_tiles[(x, y)] == 'white' else 'white'
        else:
            visited_tiles[(x, y)] = 'black'
    
    if not p2:
        return [tile_colour for tile_colour in visited_tiles.values()].count('black')  # return the number of black tiles for part 1
    else:
        return visited_tiles  # for part 2 we need the initial grid as the input - return it here


# PART 2
# Every day for 100 days - the tiles are flipped according the following rule set:
# Any black tile with zero OR more than 2 (i.e. n == 0 or n > 2) black adjacent to it is flipped to white
# Any white tile with exactly 2 black tiles adjacent to it is flipped to black
# Find the number of black tiles after 100 days - day 0 uses the tiles found in part 1

def get_neighbours(x, y):
    return [(x, y+1), (x+1, y+1), (x+1, y), (x, y-1), (x-1, y-1), (x-1, y)]  # return nw/ne/e/se/sw/w

def second_solution(initial_tiles, days):
    curr_tiles = {coord: colour for coord, colour in initial_tiles.items() if colour == 'black'} # remove white tiles from starting input

    for i in range(days):
        next_tiles = curr_tiles.copy()  # initialise the dictionary to store changes to

        for x, y in curr_tiles.keys():  # the tiles checked here are ALWAYS black - they can be removed from the next_gen if flipped
            neighbours = get_neighbours(x, y)

            black_tiles = 0
            for neighbour in neighbours:
                black_tiles += 1 if curr_tiles.get(neighbour) == 'black' else 0

            if black_tiles == 0 or black_tiles > 2:
                next_tiles.pop((x, y))  # remove the tile from the next generation
            
            for neighbour in neighbours:
                nbr_x, nbr_y = neighbour[0], neighbour[1]

                if curr_tiles.get((nbr_x, nbr_y), 'white') == 'black':  # if the tile is black, it may have / will be checked - skip it here!
                    continue

                n_neighbours = get_neighbours(nbr_x, nbr_y) # get the neighbours of the neighbouring tile
                black_tiles = 0
                for n_neighbour in n_neighbours:  # check the colours of the neighbour's neighbours
                    black_tiles += 1 if curr_tiles.get(n_neighbour) else 0

                if black_tiles == 2:
                    next_tiles[(nbr_x, nbr_y)] = 'black'
  
        curr_tiles = next_tiles

    return len(next_tiles)

# tests
print(first_solution(tiles))
print(second_solution(first_solution(tiles, p2=True), 100))