d1 = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/2015/Day1.1.txt", 'r')

# PART 1
# Start at floor 0, ( is +1, ) is -1
content = d1.read()

def final_floor(instructions):
    floor = 0
    for char in instructions:
        if char == '(':
            floor += 1
        else:
            floor -= 1

    return floor

print(final_floor(content))

# PART 2
# Find the first character position which makes floor < 0

def basement_floor(instructions):
    floor = 0
    index = 0

    for char in instructions:
        index += 1
        if char == "(":
            floor += 1
        else:
            floor -= 1
        
        if floor < 0:
            return index

    return "You never visit the basement!"

print(basement_floor(content))