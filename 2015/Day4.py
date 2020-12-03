part1_input = 'bgvyzdsv'
import hashlib

# PART 1
# Get the positive integer value which when appended to the input produces an MD5 hash key - first 5 digits are 0 in hex

def hash_generator(input_string, num_zeroes):
    i = 1

    # literally just cycle through all the damn things
    while True:
        test_input = f"{input_string}{i}" 

        value = hashlib.md5(test_input.encode())
        hashkey = value.hexdigest()

        # check if the first n digits of the hash are equal to the string of zeroes
        if str(hashkey[:num_zeroes]) == ("0" * num_zeroes):
            return i, hashkey
        
        i += 1

# pick a god and pray
print(hash_generator(part1_input, 5))
print(hash_generator(part1_input, 6))
# print(hash_generator(part1_input, 7)) -- this takes to long lmao