day1_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/1.1.txt", 'r')

# put all the entries in a single list of integer values
entries = []
for item in day1_file:
    entries.append(int(item))

# PART 1
# Find 2 numbers in the list whose sum is 2020 and return their product
def twentytwenty_2(entry_list):
    i = 0

    for number in entry_list:
        i += 1
        for num_to_test in entry_list[i:]:
            if number + num_to_test == 2020:
                answer = number * num_to_test
                return answer

    return "No two values in the list added up to 2020, try again!"

# PART 2
# Find 3 numbers in the list whose sum is 2020 and return their product
def twentytwenty_3(entry_list):
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
    
    return "No three values in the list added up to 2020, try again!"

# notes
# for testing 3 numbers, if a + b >= 2020 --> do not test for a third number
# there are a lot of valid combos to work through, you want to avoid repetitions, shrink the list, avoid self-counting a/b during c-check


# test fucntion + cases
print("Testing 2 Int Sums...")
print(twentytwenty_2([1, 2, 3, 4, 5, 6, 2021, 2022, 1980, 1999, 2016]))  # should return 8064
print(twentytwenty_2([1721, 979, 366, 299, 675, 1456])) # should return 514579
print(twentytwenty_2(entries)) 
print("Testing 3 Int Sums...")
print(twentytwenty_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2020, 2018])) # should return 2018
print(twentytwenty_3([1721, 979, 366, 299, 675, 1456])) # should return 241861950
print(twentytwenty_3(entries)) 
