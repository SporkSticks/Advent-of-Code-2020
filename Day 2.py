day2_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/2.1.txt", 'r')
password_list = day2_file.read().split("\n")

# PART 1
# checks if a given password is valid by checking if the number of times the character appears lays within the range (min-max inclusive)

# tallies up the number of correct passwords from a list by passing the organised values into the password_check function
# each password is in the form --> "min-max letter: password"
def first_solution(passwords):
    total = 0

    for password_data in passwords:
        split_data = password_data.split()
        password = split_data[2]
        character = split_data[1][0]
        
        range_data = split_data[0].split("-")
        min_num, max_num = int(range_data[0]), int(range_data[1])

        total += min_num <= password.count(character) <= max_num

    return total


# PART 2
# checks if a given password has **exactly** one character in the one-indexed positions provided
# e.g. 1-3 a: abcde is valid --> 'a' is in position 1 but not 3

def password_check2(pos1, pos2, character, password):
    pass_len = len(password)

    if pos1 > pass_len or pos2 > pass_len:
        return 0

    pos1true = password[pos1 - 1] == character
    pos2true = password[pos2 - 1] == character

    return pos1true ^ pos2true


def second_solution(passwords):
    total = 0

    for password_data in passwords:
        split_data = password_data.split()
        password = split_data[2]
        character = split_data[1][0]
        
        range_data = split_data[0].split("-")
        pos1, pos2 = int(range_data[0]), int(range_data[1])

        total += password_check2(pos1, pos2, character, password)

    return total

# tests
print(first_solution(password_list))
print(second_solution(password_list))
