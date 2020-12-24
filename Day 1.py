day1_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/1.1.txt", 'r')
entries = [int(num) for num in day1_file.read().split("\n")]

# PART 1
# Find 2 numbers in the list whose sum is 2020 and return their product
def first_solution(entry_list):
    i = 0

    for number in entry_list:
        i += 1
        for num_to_test in entry_list[i:]:
            if number + num_to_test == 2020:
                answer = number * num_to_test
                return answer

# PART 2
# Find 3 numbers in the list whose sum is 2020 and return their product
def second_solution(entry_list):
    i = 0

    for a in entry_list:
        i += 1
        copy_list = entry_list[i:]
        for b in entry_list[i:]:
            if a + b >= 2020:
                continue
            else:
                copy_list.remove(b)
                for c in copy_list:
                    if a + b + c == 2020:
                        return a * b * c
            
# tests
print(first_solution(entries)) 
print(second_solution(entries)) 
