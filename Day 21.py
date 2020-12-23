day21_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/21.1.txt", 'r')
content = day21_file.read().split('\n')

# break the input into a manageable form of [ [[ingredients], [allergens]] , [[x], [y]], ... ], store the known allergens in a separate set
food_list = {}
known_allergens = set()
for i, line in enumerate(content):
    line = line.split(" (contains ")
    ingredients, allergens = line[0].split(), line[1].rstrip(")").replace(",", "").split()
    food_list[i] = [ingredients, allergens]

    for allergen in allergens:
        known_allergens.add(allergen)

# PART 1
# You have been given a list of foods - they have their ingredients and potential allergens listed out
# You must find the total number of times ingredients which CANNOT be an allergen appear in the foods list

def first_solution(food_list, known_allergens):
    non_allergens, potential_allergens = [], []  # potential allergens is for our mystery language allergen equivalents
    known_count = len(known_allergens)  
    
    while True:  # this will be run until we have found a mystery language version of each allergen
        if len(potential_allergens) == known_count:
            break

        value_copies = list(food_list.values())    
        for food in value_copies:  # we want to check against foods which only contain 1 allergen to prevent ambiguities

            ingredients, allergens = food[0], food[1]
            temp_allergens = set(ingredients)
            if len(allergens) != 1:
                continue
            else:
                for food in value_copies:           # find ingerdients common to all foods containing the allergen - these are potential IDs
                    if allergens[0] in food[1]:
                        temp_allergens = temp_allergens.intersection(food[0])

                    if len(temp_allergens) != 1: # if more than 1 possible allergen is identified, we cannot determine its ID - move on  
                        continue
                    else:                        # at this stage we have identified an allergen with only 1 possible ID
                        potential_allergens.append([list(temp_allergens)[0], allergens[0]])
                        foreign_allergen, english_allergen = potential_allergens[-1][0], potential_allergens[-1][1]

                        # remove missed allergens which may have been skipped in previous push-downs
                        non_allergens = [x for x in non_allergens if x != foreign_allergen]       

                        for i, re_food in enumerate(value_copies):
                            re_ingredients, re_allergens = re_food[0], re_food[1]
                            
                            if i not in food_list.keys():
                                continue
             
                            if english_allergen in re_allergens:
                                re_allergens.remove(english_allergen)
                                re_ingredients.remove(foreign_allergen)

                                if not re_allergens:
                                    non_allergens += re_ingredients
                                    food_list.pop(i)
                                else:
                                    food_list[i] = [re_ingredients, re_allergens]  
       
                    break
    
    # this is so scuffed but i found the allergens so i just count all of them and subtracted the num_times the allergens occur
    day21_file = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/Input Files/21.1.txt", 'r')
    content = day21_file.read().split('\n')
    ingredients = []
    for line in content:
        line = line.split(" (contains ")
        ing = line[0].split()
        ingredients += ing

    return len(ingredients) - sum([ingredients.count(allergen[0]) for allergen in potential_allergens]), potential_allergens

# PART 2
# Return your ingredients list in alphabetical order with commas
def second_solution(allergens):
    return ','.join([x[0] for x in sorted(allergens, key = lambda x: x[1])])

# tests
part1_answer, part2_input = first_solution(food_list, known_allergens)
print(part1_answer)
print(second_solution(part2_input))
