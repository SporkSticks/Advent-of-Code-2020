import re
day4_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/4.1.txt", 'r')
content = day4_file.read().split("\n\n")

# go through each line, replacing newline spaces, splitting each key value pair up, and assigning them into a unique dictionary
passport_dict_list = []
for passport in content:
    field_values = passport.replace('\n', ' ').split()
    passport_keyvals = [keypair.split(":") for keypair in field_values]
    passport_dict_list.append({k:v for k, v in passport_keyvals})

# PART 1
# Work through the passport listings in the file to find the total number of possports which are valid
# A valid passport has every expected field [byr, iyr, eyr, hgt, hcl, ecl, pid] ignoring the optional field [cid]
def first_solution(passport_list):
    num_valid = 0
    fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}  # 'cid' is not required
    num_fields = len(fields)

    for passport_dict in passport_list:
        pass_fields = set(passport_dict.keys())     
        if len(pass_fields & fields) == num_fields:   # get the intersection b/w the fields present/required sets
            num_valid += 1

    return num_valid

# PART 2
# Now each passport must have its credential values validated, still ignoring ['cid'] 
def second_solution(passport_list):
    num_valid = 0
    fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}  # 'cid' is not required
    num_fields = len(fields)

    for passport_dict in passport_list:
        pass_fields = set(passport_dict.keys())     
        if len(pass_fields & fields) == num_fields and isValid(passport_dict):    # short circuit to ensure only "complete" passports are checked
            num_valid += 1

    return num_valid

# keep the check function separate to keep things clean
def isValid(pass_dict):
    eye_cols = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    # get the height value to make comparison easier in the final check
    height_val = pass_dict['hgt']
    if 'cm' not in height_val and 'in' not in height_val:
        return 0
    else:
        height_type = height_val[-2:]
        height = int(height_val[:-2])

    if ((1920 <= int(pass_dict['byr']) <= 2002) and
        (2010 <= int(pass_dict['iyr']) <= 2020) and 
        (2020 <= int(pass_dict['eyr']) <= 2030) and 
        ((150 <= height <= 193) if height_type == 'cm' else (59 <= height <= 76)) and
        (re.match("^#[0-9a-f]{6}$", pass_dict['hcl'])) and 
        (pass_dict['ecl'] in eye_cols) and
        (len(pass_dict['pid']) == 9 and pass_dict['pid'].isnumeric())):
        return 1
    else:
        return 0 

# tests
print(first_solution(passport_dict_list))
print(second_solution(passport_dict_list))

# PART 2 constraints
# byr/iyr/eyr --> 4 digits - byr[1920, 2002], iyr[2010, 2020], eyr[2020, 2030]
# hgt --> num followed by 'cm' or 'in' - cm[150, 193], in[59, 76]
# hcl --> # followed by six chars (0-9) or (a-f) --> hex value
# ecl --> only one of [amb, blu, brn, gry, grn, hzl, oth]
# pid --> nine digit number (including leading zeroes)
