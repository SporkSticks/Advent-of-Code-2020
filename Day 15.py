puzzle_input = [18, 8, 0, 5, 4, 1, 20]

# PART 1
# You play a never ending memory game which utilises the puzzle input and each player takes turns saying a number related to the previous number
# If the last spoken number has *not been spoken before* the current player says 0
# Otherwise if the previous number *has been spoken before* the current player states the number of turns since that number was last said
# The first turns are spent reading out the inputs - without applying the rules above 
# Find the 2020th number spoken

def first_solution(starting_nums, final_turn):
    spoken_history = {} # initialise dictionary to store values spoken 

    for i in range(len(starting_nums)):
        spoken_history[starting_nums[i]] = i + 1  # store each value with its turn value

    last_num = starting_nums[-1]
    for i in range(len(starting_nums) + 1, final_turn + 1):  # offset +1 to start and end at the correct turn value 

        num = i - 1 - spoken_history[last_num] if last_num in spoken_history else 0   # get i - turn_spoken if an old number, else 0

        spoken_history[last_num] = i - 1    # store the number with the turn it was spoken on
        last_num = num

    return last_num
    
# PART 2
# Now find the 30,000,000th number spoken :)

# tests
print(first_solution(puzzle_input, 2020))
print(first_solution(puzzle_input, 30000000))