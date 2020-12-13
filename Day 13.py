day13_file = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/Input Files/13.1.txt", 'r')
bus_schedule = day13_file.read().split('\n') 

# PART 1
# You have two inputs - a timestamp and a list of bus IDs --> the timestamp is the earliest time you can depart the airport
# The list of IDs indicates how often a bus departs from time 0 --> e.g. bus ID 5 (0, 5, 10, 15, ...) - bus IDs of 'x' are unavailable
# You must find the time after the timestamp in which the earliest bus departs multiplied by the ID of that bus

def first_solution(bus_schedule):
    timestamp, bus_ids = int(bus_schedule[0]), sorted([int(bus) for bus in bus_schedule[1].split(',') if bus != 'x'])

    time_to_next_bus = [((bus_id - timestamp % bus_id), bus_id) for bus_id in bus_ids]  # find time after the timestamp each bus will arrive
    earliest_time, soonest_bus_ID = time_to_next_bus[0][0], time_to_next_bus[0][1]

    return earliest_time * soonest_bus_ID

# PART 2
# You must now find the timestamp such that every bus in your schedule is offset correctly according to the list spacing
# e.g. ['17', 'x', '13', '19'] aligns with 3417 --> 17/3417, 13/3419, 19/3420 - note the 'x' increases the offset by 1

def second_soltuion(bus_schedule):
    bus_ids = bus_schedule[1].split(',')
    timestamp, increment = 0, 1

    # simplified version of the chinese remainder theorem since the remainder values should always be 0 (i.e. time + index % id == 0)
    # work through each value, incrementing using the searching id to find a value which is 0
    # e.g. [17, x, 13, 19] -- 0 + 0 % 17 == 0 -- 102 + 2 % 13 == 0 -- 3417 + 3 % 19 == 0 -- 3419 is the answer
    for index, bus_id in enumerate(bus_ids):
        if bus_id == 'x':
            continue
        while (timestamp + index) % int(bus_id) != 0:
            timestamp += increment
        increment *= int(bus_id)

    return timestamp
      
# tests
print(first_solution(bus_schedule))
print(second_soltuion(bus_schedule))