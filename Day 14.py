day14_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/14.1.txt", 'r')
initialisation_commands = day14_file.read().split('\n') 

# PART 1
# You are given a list of init commands which can either be a 36-bit unsigned bitmask or a memory assignment (e.g. mem[address] = value)
# When a value is written to memory - the bitmask is applied to the value prior to being written to memory
# The bitmask can have 0, 1, or X as bit values --> an X at position n means no mask should be applied at that position
# You must find the sum of all values currently in working memory following the initialisation commands

def first_solution(init_cmds):
    memory_dict, bitmask = {}, init_cmds[0].split(' = ')[1]

    for cmd in init_cmds:
        if cmd.split()[0] == 'mask':
            bitmask = cmd.split(' = ')[1]  # new bitmask is being assigned
        else:
            address, value = int(cmd.split(' = ')[0][4:-1]), int(cmd.split(' = ')[1]) # get the memory location and the value to store
            value_36bit = [bit for bit in format(value, '036b')] # convert integer into 36 bit string

            for nth_bit, bit in enumerate(bitmask):
                if bit == 'X':
                    continue
                else:
                    value_36bit[nth_bit] = bit  # apply the mask at the nth bit

            memory_dict[address] = int(''.join(value_36bit), 2) # add the masked value to the memory dict as a base-10 converted integer

    return sum(memory_dict.values())  # return the sum of all integers in memory

# PART 2
# The list of commands is actually written such that a group of values can be assigned at a given memory address using the bitmask on the value
# In this case 0/1 still mask the same way, but 'X' creates a floating bit - which can be 1 or 0 --> e.g. X10X --> 0100 0101 1100 1101 
# Return the sum of all the integers stored in memory at the end of the initialisation commands

def second_solution(init_cmds):
    memory_dict, bitmask = {}, init_cmds[0].split(' = ')[1]

    for cmd in init_cmds:
        if cmd.split()[0] == 'mask':
            bitmask = cmd.split(' = ')[1]
        else:
            input_address, value, target_addresses = int(cmd.split(' = ')[0][4:-1]), int(cmd.split(' = ')[1]), []
            value_36bit = [bit for bit in format(input_address, '036b')]

            # apply the bitmask to the input memory address and count the number of floating bits
            for nth_bit, bit in enumerate(bitmask):
                if bit == '0':
                    continue
                elif bit == '1':
                    value_36bit[nth_bit] = '1'
                else:
                    value_36bit[nth_bit] = 'X'

            floating_bit_count = value_36bit.count('X') 

            # replace all the floating bit values to get the addresses to store the command value
            for i in range(2 ** floating_bit_count):  # the number addresses is equal to 2 ^ (num of 'X') // e.g. n=2 - 00, 01, 10, 11
                floating_bit = f"{i:>0{floating_bit_count}b}"  # get the ith binary corresponding to the ith address
                address = ''

                # replace the kth floating bit 'X' with the kth bit in the floating bit
                k = 0  
                for bit in value_36bit:
                    if bit != 'X':
                        address += bit
                    else:
                        address += floating_bit[k]
                        k += 1

                target_addresses.append(int(address, 2))  # convert addresses to a base-10 integer

            for address in target_addresses:
                memory_dict[address] = value  # store the values in memory - overwriting where necessary

    return sum(memory_dict.values())  # return the sum of all the integers in memory


# tests
print(first_solution(initialisation_commands))
print(second_solution(initialisation_commands))
