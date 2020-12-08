day6_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/6.1.txt", 'r')
content = day6_file.read().split('\n\n')

questionnaires = [x.split('\n') for x in content]

# PART 1
# Passengers are given a 26 Question Questionnaire (a-z) - each answer can be yes or no - passengers submit their answers in groups
# Return the sum of the number of unique 'yes' responses provided by each group (e.g. 'abc' == 3, 'ab, ab' == 2, 'a' 'a' 'a' 'a' == 1)

def yes_counter(questionnaire):
    answers = ''
    for answer in questionnaire:
        answers += answer
    return len(set(answers))

def first_solution(questionnaires):
    total_yes = 0
    for questionnaire in questionnaires:
        total_yes += yes_counter(questionnaire)
    return total_yes

# PART 2
# Now find the sum of the number of questions to which everyone from each group responded 'yes' (e.g. 'ab' 'ac' == 1, 'a' 'b' == 0)

def second_solution(questionnaires):
    total_allyes = 0

    for questionnaire in questionnaires:
        num_people = 0
        answers = ''

        for answer in questionnaire:
            answers += answer
            num_people += 1

        unique_answers = set(answers)

        for letter in unique_answers:
            if answers.count(letter) != num_people:
                continue
            else:
                total_allyes += 1
 
    return total_allyes

print(first_solution(questionnaires))
print(second_solution(questionnaires))
