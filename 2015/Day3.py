d3 = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/2015/Day3.1.txt", 'r')

content = d3.read()

# PART 1 
# Find the number of unique spaces visited in the coordinates explored in the instructions > < ^ and V (right, left, up, and down)

directions = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}

def unique_spaces(instructions):
    coords = {(0, 0)}
    curr_coord = (0, 0)

    for direction in instructions:
        prev_x, prev_y = curr_coord[0], curr_coord[1]
        x, y = directions[direction][0], directions[direction][1]

        curr_coord = (prev_x + x, prev_y + y)
        coords.add(curr_coord)
        
    unique_houses = len(coords)
    return unique_houses 

print(unique_spaces(content))


# PART 2
# Now there are two Santas taking alternate movements from the same starting location, find the number of unique houses visited

def unique_2santas(instructions):
    coords = {(0, 0)}
    santa_curr = (0, 0)
    robo_santa = (0, 0)

    i = 0
    for direction in instructions:
        if i % 2:
            prev_x, prev_y = santa_curr[0], santa_curr[1]
            x, y = directions[direction][0], directions[direction][1]

            santa_curr = (prev_x + x, prev_y + y)
            coords.add(santa_curr)
        else:
            prev_x, prev_y = robo_santa[0], robo_santa[1]
            x, y = directions[direction][0], directions[direction][1]

            robo_santa = (prev_x + x, prev_y + y)
            coords.add(robo_santa)
        i += 1

    unique_houses = len(coords)
    return unique_houses

print(unique_2santas("^v")) # should return 3
print(unique_2santas("^>v<")) # should return 3
print(unique_2santas("^v^v^v^v^v")) # should return 11
print(unique_2santas(content))