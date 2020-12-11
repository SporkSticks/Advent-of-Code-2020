day10_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/10.1.txt", 'r')
content = day10_file.read().split('\n')
joltages = sorted([int(num) for num in content])
joltages.insert(0, 0) # add in the initial outlet joltage of 0  

# PART 1
# You have to charge a device using an outlet with a rating of 0 "joltages" by connecting ALL the adaptors in your input list to your
# device (not in the list) --> each adapter can take an input 1-3 "jolts" lower than it's own rating --> e.g. 0, [1, 2, 5, 8, 10, 11, ...]
# You must return the product of the total 1-jolt and 3-jolt differences in your adaptor chain - this includes your own device (+3 jolts)

def first_solution(joltages):  
    one_jump, three_jump = 0, 1    # the '1' accounts for the connection from the final adaptor to the device [..., n], n+3

    for i in range(len(joltages) - 1):
    
        if joltages[i + 1] - joltages[i] == 1:
            one_jump += 1
        elif joltages[i + 1] - joltages[i] == 3:
            three_jump += 1

    return one_jump * three_jump

# PART 2
# You must now find the total number of arrangements which correctly connect your device to the charging outlet using any number of adapters :)

def second_solution(joltages):
    final_joltage = joltages[-1]
    
    routes_to_n = {}

    routes_to_n[1] = 1 if 1 in joltages else 0
    routes_to_n[2] = routes_to_n[1] + 1 if 2 in joltages else 0
    routes_to_n[3] = routes_to_n[2] + routes_to_n[1] + 1 if 3 in joltages else 0

    for i in range(4, final_joltage + 1):
        routes_to_n[i] = routes_to_n[i-1] + routes_to_n[i-2] + routes_to_n[i-3] if i in joltages else 0

    return routes_to_n[final_joltage]

# tests
print(first_solution(joltages))
print(second_solution(joltages))
