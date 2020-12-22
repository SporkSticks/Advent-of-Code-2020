from collections import deque  # provides O(1) time queue functionality vs O(n) for lists

day22_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/22.1.txt", 'r')
content = day22_file.read().split("\n\n")

p1 = deque([int(card) for card in content[0].split("\n")[1:]])
p2 = deque([int(card) for card in content[1].split("\n")[1:]])
p3, p4 = p1.copy(), p2.copy()  # generate copies for part 2 since queues are dumb and dont pass in copies to functions

#PART 1
# You're playing a game with a crab where you place cards from the front of the deck [index 0] and compare values - the winner takes
# both cards and places them at the [i-2] and [i-1] positions in their deck (with the highest card at i-2)
# The game ends when one player runs out of cards - the winner's score is taken by multiplying the top card by the length of the deck
# e.g. 3 2 10 1 -->  3*4 + 2*3 + 10*2 + 1*1 --> return the winner's score!

def first_solution(p1, p2):

    while p1 and p2:
        p1_card, p2_card = p1.popleft(), p2.popleft()
        p1.extend([p1_card, p2_card]) if p1_card > p2_card else p2.extend([p2_card, p1_card])

    if p1:
        return f"Player 1 won: {sum([num * (i+1) for num, i in zip(list(p2)[::-1], range(len(p1)))])}"
    else: 
        return f"Player 2 won: {sum([num * (i+1) for num, i in zip(list(p2)[::-1], range(len(p2)))])}"  # it's rigged for p2 to win lol


# PART 2
# You lost to the crab :( - but you can reclaim your glory by playing the game again with recursive rules
# For each INDVIDUAL game - if both players have the same cards as in a previous round - player 1 wins instantly to prevent infinite loops!
# If both players have at least as many cards in their deck as the value of the card they just drew (excluding that card) - a new game is starts
# using copies of each deck equal in length to the value of the cards played to induce the recursive game - the winner of that game wins the 
# outer game's round --> return the winner's score using the updated rules!   // note the recursive games take cards from the LEFT of the list

def recursive_combat(p1, p2):
    prev_rounds = set()
    
    while p1 and p2:
        if (tuple(p1), tuple(p2)) in prev_rounds:
            return 1, 0  # return to indicate player 1 wins
        else:
            prev_rounds.add((tuple(p1), tuple(p2)))

        p1_card, p2_card = p1.popleft(), p2.popleft()

        if len(p1) >= p1_card and len(p2) >= p2_card:  # enter a recursive game using 
            rec_p1, rec_p2 = recursive_combat(deque(list(p1)[:p1_card]), deque(list(p2)[:p2_card]))
            p1.extend([p1_card, p2_card]) if rec_p1 else p2.extend([p2_card, p1_card])

        else:
            p1.extend([p1_card, p2_card]) if p1_card > p2_card else p2.extend([p2_card, p1_card])

    return p1, p2  # once a game is complete, return the decks - one will be empty

def second_solution(p1, p2):
    p1, p2 = recursive_combat(p1, p2)
    if p1:
        return f"Player 1 won: {sum([num * (i+1) for num, i in zip(list(p1)[::-1], range(len(p1)))])}"
    else:
        return f"Player 2 won: {sum([num * (i+1) for num, i in zip(list(p2)[::-1], range(len(p2)))])}"  # still rigged

# tests
print(first_solution(p1, p2))
print(second_solution(p3, p4))
