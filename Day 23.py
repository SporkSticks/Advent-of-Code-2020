day23_input = [4, 6, 7, 5, 2, 8, 1, 9, 3]

# PART 1
# You are still fighting the crab - you have cups in a circle labelled with the numbers in your input - this forms a circular list
# You starting cup is the first one in the list - each turn progresses as follows:
# The crab will pick up three cups clockwise of your current cup and it will select a destination cup == curr - 1 (if curr = 1, loop back to 9)
# if the destination is one of the three picked up - 1 is subtracted until a valid destination is selected
# The crab will then move the cups to be clockwise from the destination cup (preserving their order) - the next cup is 1 forward from the curr cup
# After 100 moves - return the order the cups are in clockwise from the cup labelled 1 (e.g. [4, 1, 3, 2] - return '324')

def first_solution(cups):
    n, num_cups = 0, len(cups)
    curr_cup = cups[n]

    for i in range(100):
        moved_cups = cups[(n+1) % num_cups], cups[(n+2) % num_cups], cups[(n+3) % num_cups]
        destination = (curr_cup + 7) % num_cups + 1
        while destination in moved_cups:
            destination = (destination + 7) % num_cups + 1  # (i - m + n - 1) % n + 1 --> m positions back through n items

        q = [None] * 9  # set up the new list - start by adding the curr_cup, then sliding cups across
        q[n % num_cups] = curr_cup
        while q[n % num_cups] != destination:
            n += 1
            q[n % num_cups] = cups[(n+3) % num_cups] 

        n += 1
        for index in range(3):
            q[n % num_cups] = moved_cups[index]  # add in the cups following the destination
            n += 1

        while not q[n % num_cups]:  # add in any remaining cups that were not slid across
            q[n % num_cups] = cups[n % num_cups]
            n += 1

        cups = q  # cups is now the new deque
        n += 1
        curr_cup = cups[n % num_cups]  # as the curr_cup does not move, the next cup is one index position forward
        
    return ''.join(''.join([str(n) for n in list(cups)]).split('1')[::-1])  # return the cup order working clockwise from cup 1


# PART 2
# Turns out this crab has a trick up its sleeve - they're actually now using 1,000,000 cups, the cups after the list are just += 1 from 
# the largest number (i.e. 9) - the crab will perform 10,000,000 moves! Find the product of the two cups after the cup labelled 1...

def second_solution(cups):
    cups += [x for x in range(10, 1000001)]  # add the extra cups to the list

    cup_list = [0] * 1000001  # (+1) to match index positions correctly
    
    # initialise the lookup array to store the cup index positions as neighbours with the first cup at the end
    # e.g. for [4, 6, 7, 5, 2, 8, 1, 9, 3, 10, ...] --> 4 moves to the end, 6 moves to index 4, 7 moves to index 6, 5 moves to index 2, ...
    for i in range(len(cups)):
        if i == len(cups) - 1:
            cup_list[cups[i]] = cups[0]
        else:
            cup_list[cups[i]] = cups[i+1]

    # cups need to be picked up based on their relative position to cup 1 - instead of moving every cup, we just grab their position
    # using the lookup array in O(1) time --> each neighbouring cup is stored as relative indexes from each other
    
    start = cups[0]  # get the first cup from the original list, then get the three neighbours in sequence
    for i in range(10000000):
        cup_one = cup_list[start]
        cup_two = cup_list[cup_one]
        cup_three = cup_list[cup_two]
        cup_list[start] = cup_list[cup_three]  

        # same as part 1, work backwards to get the destination, looping if necessary
        destination = start - 1
        while destination in (cup_one, cup_two, cup_three) or destination < 1:
            destination -= 1
            if destination < 1:
                destination = 1000000
        
        cup_list[cup_three] = cup_list[destination] 
        cup_list[destination] = cup_one  
        start = cup_list[start] 

    return cup_list[1] * cup_list[cup_list[1]]

# tests
print(first_solution(day23_input))
print(second_solution(day23_input))