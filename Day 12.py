day12_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/12.1.txt", 'r')
content = day12_file.read().split('\n')

# PART 1
# The ferry you are on is heading into a storm - you have the instructions to get to safety in the form of the input list
# N/E/S/W move n units in the given cardinal directions - L/R turns the boat n degrees - F moves forward n units in the direction the boat faces
# You must find the Manhatten distance (sum of absoulte W/E pos + absolute N/S pos) from your starting position

directions = {0: 'N', 90: 'E', 180: 'S', 270: 'W', 'L': -1, 'R': +1}
cardinal = {'N': +1, 'S': -1, 'E': +1, 'W': -1}

def first_soltuion(instruction_list):
    boat_x, boat_y, rotation = 0, 0, 90  # starting at the origin, facing right

    for instruction in instruction_list:
        operation, value = instruction[0], int(instruction[1:])

        if operation in ['N', 'S']:
            boat_y += value * cardinal[operation]   # move up/down
        elif operation in ['W', 'E']:
            boat_x += value * cardinal[operation]   # move left/right
        elif operation in ['L', 'R']:
            rotation = (rotation + directions[operation] * value) % 360  # rotate the boat and keep the value within 0-270
        elif operation == 'F':
            if rotation == 0 or rotation == 180:  
                boat_y += value * cardinal[directions[rotation]]  # boat is facing N/S
            else:
                boat_x += value * cardinal[directions[rotation]]  # boat is facing E/W
            
    return abs(boat_x) + abs(boat_y)

# PART 2
# The instructions actually describe the ship moving relative to a waypoint which starts 10 units East, and 1 unit North of the ship (10, 1)
# N/E/S/W/L/R all move the waypoint relative to the ship - only F moves the ship, n times toward the waypoint (which moves with the ship)
# e.g. F10 as a first instruction will move the ship 10 times --> 100 units east, and 10 north - the waypoint is still locally at (10, 1)

def second_solution(instruction_list):
    boat_x, boat_y, waypoint_x, waypoint_y, waypoint_rot = 0, 0, 10, 1, 90

    for instruction in instruction_list:
        operation, value = instruction[0], int(instruction[1:])

        if operation in ['N', 'S']:
            waypoint_y += value * cardinal[operation]
        elif operation in ['W', 'E']:
            waypoint_x += value * cardinal[operation]
        elif operation in ['L', 'R']:
            rotation = (directions[operation] * value) % 360 # get the rotation as a value representing the clockwise rotation
            if rotation:
                if rotation == 90:
                    waypoint_x, waypoint_y = waypoint_y, -waypoint_x
                elif rotation == 180:
                    waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
                elif rotation == 270:
                    waypoint_x, waypoint_y = -waypoint_y, waypoint_x         
        elif operation == 'F':
            boat_x += value * waypoint_x
            boat_y += value * waypoint_y

    return abs(boat_x) + abs(boat_y)
        
# tests
print(first_soltuion(content))
print(second_solution(content))
