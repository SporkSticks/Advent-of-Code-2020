import nltk

day19_file = open("C:/Users/[REDACTED]/Desktop/Advent of Code 2020/Input Files/19.1.txt", 'r')
content = day19_file.read().split('\n\n')
content[0] = "\n".join(sorted(content[0].replace(':', " ->").split("\n")))

# create the grammar used in part 1 --> in the form (S -> 1 \n T -> S | 1 \n ...)
grammar1, messages = nltk.CFG.fromstring(content[0]), [" ".join(string) for string in content[1].split('\n')]

# implement the changes to the grammar introduced in part 2: change rules 8 and 11
content[0] = content[0].replace("8 -> 42", "8 -> 42 | 42 8").replace("11 -> 42 31", "11 -> 42 31 | 42 11 31")
grammar2 = nltk.CFG.fromstring(content[0])

# PART 1
# You are given a rule set and a list of messages to validate - the rule set is numbered and build on each other
# For example --> (0: 1 2 -- 1: 'a' -- 2: 1 3 | 3 1 -- 3: 'b') --> to obey rule 0 - an input must be in the form that obeys rules 1 then 2
# Rules with a pipe can be satisfied in either order --> for rule 0, it must start with an 'a', then be followed by 'ab' or 'ba'
# You must find the number of messages which obey rule 0 in your input

def first_solution(grammar1, textlist):
    count, parser = 0, nltk.parse.BottomUpLeftCornerChartParser(grammar1)

    for text in textlist:
        print(text, count)
        sentence = nltk.word_tokenize(text)  # break the string into tokens for analysis
        if parser.parse_one(sentence):  # this returns a tree with the solution of a match or None if a probable solution is not found
            count += 1

    return count

# PART 2
# Rules 8 and 11 were printed incorrectly - they are 8: 42 | 42 8 and 11: 42 31 | 42 11 31 - this introduces loops
# Find the number of valid messages after these changes

def second_solution(grammar2, textlist):
    count, parser = 0, nltk.parse.BottomUpLeftCornerChartParser(grammar2)

    for text in textlist:
        print(text, count)
        sentence = nltk.word_tokenize(text)
        if parser.parse_one(sentence):
            count += 1

    return count

# tests
print(first_solution(grammar1, messages))
print(second_solution(grammar2, messages))
