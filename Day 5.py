day4_file = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/Input Files/5.1.txt", 'r')
content = day4_file.read()
boarding_pass_list = content.split()

# PART 1
# You have to find the highest seat ID in a list of boarding passes - plane has 128 rows and 8 columns
# each pass is 10 chars long --> first 7 chars find the row through binary search - last 3 chars find the column similarly
# the Seat ID is found by (row * 8 + col)

def seat_id(boarding_pass):
    row, col = '0b', '0b'
    row_str, col_str = boarding_pass[:7], boarding_pass[7:]
       
    for letter in row_str:
        row += '0' if letter == 'F' else '1'
    for letter in col_str:
        col += '0' if letter == 'L' else '1'

    return (int(row, 2) * 8 + int(col, 2))

def first_solution(pass_list):
    highest_id = 0
    for boarding_pass in pass_list:
        curr_id = seat_id(boarding_pass)
        if curr_id > highest_id:
            highest_id = curr_id   

    return highest_id

# PART 2
# Now you have to find your OWN seat ID - every seat should be full in the 1024 seater plane - your list has 908 IDs - yours lies within a gap
# +1 and -1 from your ID

def second_solution(pass_list):  
    ids = set()

    for boarding_pass in pass_list:
        ids.add(seat_id(boarding_pass))

    ids = list(ids)
    for i in range(len(ids)):
        if ids[i+1] - ids[i] != 1:
            return ids[i] + 1

# tests
print(seat_id('BFFFBBFRRR'))  # 567
print(seat_id('FFFBBBFRRR'))  # 119
print(seat_id('BBFFBBFRLL'))  # 820
print(first_solution(['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL'])) # 820
print(first_solution(boarding_pass_list))
print(second_solution(boarding_pass_list))