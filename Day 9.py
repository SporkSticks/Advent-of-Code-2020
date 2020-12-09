day9_file = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/Input Files/9.1.txt", 'r')
content = day9_file.read().split('\n')
num_inputs = [int(num) for num in content]

# PART 1
# You are given a list of numbers - the first 25 numbers are random - and each number after that is produced by summing two of the previous
# 25 numbers --> find the number in the list which is NOT possible to make using the previous 25 numbers before it 

def first_solution(input_list):
    min_i, max_i = 0, 25
    curr_num = input_list[25]

    for i in range(len(input_list) - 25):
        num_range = input_list[min_i : max_i]

        for num1 in num_range:
            test_nums = num_range.copy()   # make a copy of the list without num1 to avoid double counting
            test_nums.remove(num1)
            has_match = False

            for num2 in test_nums:
                if num1 + num2 == curr_num:  # if a match is found stop checking numbers and break out of the nested loops
                    has_match = True
                    break           
                    
            if has_match:  # once a match is found break out of the nested loop to avoid repeats
                break             
        
        if not has_match:
            return curr_num  # if no match was found the match trigger is never valid - return the value which has no match
        
        min_i += 1
        max_i += 1
        curr_num = input_list[max_i] # increment the test list forward by 1 index value and test the next list number

    return 'No matches were found!'

# PART 2
# Using your answer to part 1 - return the sum of the smallest and largest values within a contiguous list of numbers from your list
# which sum to your part 1 value --> e.g. if n = 8, and [3, 4, 1] is your list --> return 1 + 4 = 5

def second_solution(input_list, goal_num):
    max_val = input_list.index(goal_num)

    for start_idx in range(max_val):
        end_idx = start_idx + 1

        for i in range(max_val):   
            input_range = input_list[start_idx : end_idx + 1]   # get the input range to test
            total = sum(input_range)

            if total == goal_num:
                sorted_range = sorted(input_range)
                return sorted_range[0] + sorted_range[-1]   # return the sum of the lowest / highest values in the range
            elif total > goal_num:                          # move to the next start value if the sum overshoots the goal number
                break
            else:
                end_idx += 1    # incrememnt the end index to expand the list
            
    return "No values add up to the goal number!"

# tests
print(first_solution(num_inputs))
print(second_solution(num_inputs, first_solution(num_inputs)))