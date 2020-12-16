day16_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/16.1.txt", 'r')
train_ticket_document = day16_file.read().split('\n\n')

field_ranges = train_ticket_document[0].split('\n')
personal_ticket = train_ticket_document[1].split('\n')[1].split(',')
other_tickets = train_ticket_document[2].split('\n')[1:]

# PART 1
# You have a train ticket with values for fields which you cannot decipher - however you do know which fields they could be in addition
# to valid ranges for each said field - your input contains these ranges, your ticket numbers, and the numbers on other tickets
# You must find the sum of all the values (error rate) on each ticket which are impossible to have for **any** of the field ranges in the input

def first_solution(fields, other_tickets):
    valid_nums, error_rate = set(), 0

    # get the range of valid numbers and store them as a set
    for field in fields:
        ranges, range_list = field.split(': ')[1].split(' or '), []
        range_list.append(ranges[0].split('-'))  # lower range
        range_list.append(ranges[1].split('-'))  # upper range

        for vals in range_list:
            for i in range(int(vals[0]), int(vals[1]) + 1):
                valid_nums.add(i) # add values into the set within the provided ranges, repeat numebrs are skipped

    for i in range(len(other_tickets)):
        ticket_entries, isValid = other_tickets[i].split(','), True

        for entry in ticket_entries:
            if int(entry) not in valid_nums:
                isValid = False
                error_rate += int(entry)

        if isValid:
            valid_tickets.append(other_tickets[i].split(','))  # store the valid ticket values in an array to be used in part 2

    return error_rate   

# PART 2
# Discard all the tickets with values which cannot exist - using the remaining tickets, you can identify which of the 20 fields are which
# You must return the product of the 6 values on your own ticket which have fields beginning with the word 'departure'

valid_tickets = []  # list is filled in the call to the part 1 function (lines 34-35)

def field_range_generator(num_range):
    ranges = '-'.join(num_range.split(' or '))
    return [int(n) for n in ranges.split('-')]  # returns the ranges in the form [low1, low2, high1, high2]

def second_solution(fields, personal_ticket, valid_tickets):
    field_dict, field_indices, confirmed_fields = {}, {i:[] for i in range(0, len(fields))}, {}

    # generate the ranges for each field
    for field in fields:
        field, num_range = field.split(': ')[0], field.split(': ')[1]
        field_dict[field] = field_range_generator(num_range)

    # find all the possible index positions a given field can have (there is overlap so the first 'possible' value may not be the correct one)
    for field, values in field_dict.items():

        for index in range(len(fields)):
            allValid = True

            for ticket in valid_tickets:
                field_entry = int(ticket[index])
                if (values[0] <= field_entry <= values[1]) or (values[2] <= field_entry <= values[3]):
                    continue
                else:
                    allValid = False
                    break  # if a field cannot be at this index position, break out and try the next one

            if allValid:
                field_indices[index].append(field)  # add the potential field to this index position's list

    # work through the field dictionary, finding the list with only one possible index value all fields are assigned an index
    old_fields = set()
    for i in range(len(fields)):
        for index, fields in field_indices.items():
            
            if len(fields) == i:
                i+=1 
                confirmed_fields[index] = [x for x in fields if x not in old_fields]   
                for field in fields:
                    old_fields.add(field)
                break

    # get the values from your own ticket with 'departure' in the field name and calculate their product
    departure_product = 1
    indices = [k for k, v in confirmed_fields.items() if 'departure' in v[0]]
    
    for index in indices:
        departure_product *= int(personal_ticket[index])
        
    return departure_product

# tests
print(first_solution(field_ranges, other_tickets))
print(second_solution(field_ranges, personal_ticket, valid_tickets))
