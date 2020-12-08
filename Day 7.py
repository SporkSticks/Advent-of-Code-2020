day7_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/7.1.txt", 'r')
content = day7_file.read().replace('.', '').split('\n')

# generate a dictionary of bag dicts in the form --> {colour: {colour:num, colour:num}, colour: {colour:num}, ...}
bag_colour_rules = {}
for rule in content:
    rules = rule.replace(" bags contain", ',').split(', ')
    colour, inner_bags = rules[0], {' '.join(rule.split()[1:3]) : rule.split()[0] for rule in rules[1:]}
    bag_colour_rules[colour] = inner_bags

# PART 1
# You are given a list of rules for a LOT of different coloured bags, and the number and colours of bags they contain
# You have to find the number of colours which can contain a 'shiny golden' bag using the rule list
def inside(bag):
    if bag == 'other bags':
        return 0

    inner_colours = bag_colour_rules[bag]
    
    if 'shiny gold' in inner_colours:
        return 1
    else:
        for bag_colour in inner_colours:
            if inside(bag_colour):
                return 1
        return 0

def first_solution(bag_rules):
    contains_shinygold = 0

    for colour in bag_rules:
        contains_shinygold += inside(colour)

    return contains_shinygold

# PART 2
# Now find the number of bags inside a single gold bag (code should work for any bag!)
def second_solution(start_bag):
    if 'other bags' in start_bag:  # rare case the bag is empty {'other bags': 'no'}
        return 0

    total_bags = sum(int(count) for count in start_bag.values())

    for bags, num_bags in start_bag.items():
        total_bags += second_solution(bag_colour_rules[bags]) * int(num_bags)

    return total_bags

# tests
print(first_solution(bag_colour_rules)) # 139
print(second_solution(bag_colour_rules['shiny gold']))
print(second_solution(bag_colour_rules['dotted teal']))  # should return 0 - empty bag
