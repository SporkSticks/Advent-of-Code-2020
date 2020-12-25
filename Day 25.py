day25_file = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/Input Files/25.1.txt", 'r')

# PART 1
# You get to the hotel but their registration is offline - you cannot use your room key for your 25th floor suite (the elevator is broken)
# To unlock the door you must perfrom a cryptographic handshake testing your own inputs by transforming a subject number - 7
# To transform a subject number --> start with 1 --> then for a number of times called the loop size (the door/card use different secret values):
# --> set the value to itself * subject num --> set the value to the remainder after / by 20201227
# A handshake runs as follows:
# The card transforms the subject number of 7 according to its secret loop size - result is the card's public key
# The door transforms the subject number of 7 according to its secret loop size - result is the door's public key
# The card and door transmit their two public keys to each other (this is your input!)
# The card/door transforms the subject number of the door's/card's public key to get the *same* encryption key - you must find this value!

public_keys = day25_file.read().split('\n')
card_public, door_public = int(public_keys[0]), int(public_keys[1])

def first_solution():
    secret_loop_size, value, subject_number = 1, 1, 7  # set the initial values for the secret loop, value, and subject number
    found_card, found_door = False, False

    while not (found_card and found_door):  # iterate through each loop value until secret loop values for the door and card are found
        value *= subject_number
        value %= 20201227
        
        if value == card_public:
            found_card = secret_loop_size
        if value == door_public:
            found_door = secret_loop_size
        
        secret_loop_size += 1

    value = 1
    for i in range(found_card):  # get the encryption key for the card
        value *= door_public
        value %= 20201227
    card_encrypt = value
    return card_encrypt # the code is correct so its just faster to return the value here - remove the line to compare both codes!

    value = 1
    for i in range(found_door):  # get the encyrption key for the door 
        value *= card_public
        value %= 20201227
    door_encrypt = value

    if card_encrypt == door_encrypt:  # check the encryption keys match
        return card_encrypt
    else:
        return "You didn't find a match, your encyrption values are incorrect!"

# PART 2 --> You just needed to have all the other stars, there is no part 2 :)
# tests
print(first_solution())