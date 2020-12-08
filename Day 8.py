day8_file = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/Input Files/8.1.txt", 'r')
content = day8_file.read().split('\n')

# PART 1
# You are given a list of input instructions which revolve around a global accumulator variable 'acc'
# acc inputs change the value of the accumulator // jmp moves to a line specified by the value // nop does nothing, moves to next line
# You must find the value of the accumulator prior to an instruction being called again (i.e. a line is called twice)

def first_solution(input_list):
    acc, index = 0, 0
    used_inputs, num_inputs = [], len(input_list)

    while (index < num_inputs):
        line = input_list[index].split()
        operator, value = line[0], int(line[1])

        if ((input_list[index], index) in used_inputs):
            return acc, False  # returns the accumulator with a failed termination status
        
        if operator == 'nop':
            used_inputs.append((' '.join(line), index))
            index += 1
        elif operator == 'acc': 
            used_inputs.append((' '.join(line), index))
            acc += value
            index += 1
        else:         
            used_inputs.append((' '.join(line), index))
            index += value
    
    return acc, True   # returns the accumulator with a success termination status

# PART 2
# It is revealed that ONE 'nop' is supposed to be a 'jmp' (or vice versa) - fixing this will stop the infinte loop found in part 1
# You must find the value of the accumulator when the fixed input list is executed

def second_solution(input_list):
    index = 0
    
    for line in input_list:
        input_copy, operator, value = input_list.copy(), line.split()[0], line.split()[1]
        operator = 'nop' if operator == 'jmp' else 'acc'
        input_copy[index] = operator + ' ' + value

        termination_check = first_solution(input_copy)
        acc, terminated = termination_check[0], termination_check[1]

        if terminated:            
            return acc   
        else:
            index += 1   
            
    return 'No successful switches found.'

# tests
print(first_solution(content))
print(second_solution(content))