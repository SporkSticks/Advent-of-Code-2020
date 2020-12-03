day2_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/2.1.txt", 'r')

# put all the passwords into a single list
raw_passwords = day2_file.read()
password_list = raw_passwords.split('\n')

# PART 1
# checks if a given password is valid by checking if the number of times the character appears lays within the range (min-max inclusive)
def password_check1(min_num, max_num, character, password):
    return min_num <= password.count(character) <= max_num


# tallies up the number of correct passwords from a list by passing the organised values into the password_check function
# each password is in the form --> "min-max letter: password"
def pass_counter1(passwords):
    total = 0

    for password_data in passwords:
        split_data = password_data.split()
        password = split_data[2]
        character = split_data[1][0]
        
        range_data = split_data[0].split("-")
        min_num, max_num = int(range_data[0]), int(range_data[1])

        total += password_check1(min_num, max_num, character, password)

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

def pass_counter2(passwords):
    total = 0

    for password_data in passwords:
        split_data = password_data.split()
        password = split_data[2]
        character = split_data[1][0]
        
        range_data = split_data[0].split("-")
        pos1, pos2 = int(range_data[0]), int(range_data[1])

        total += password_check2(pos1, pos2, character, password)

    return total


# test function + cases
print(pass_counter1(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]))  # should return 2
print(pass_counter1(password_list))

print(pass_counter2(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"])) # should return 1
print(pass_counter2(["3-11 b: adbc"])) # should return 1
print(pass_counter2(password_list))
