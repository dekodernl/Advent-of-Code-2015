import hashlib

def get_input():
    f = open('puzzle-input.txt', "r")
    return f.readlines()

def solution(string):
    # rule 1 - contains two pairs of two letters
    pairs = []
    two_pairs_found = False
    for i in range(0, len(string.strip()) - 1):
        pairs.append(string[i] + string[i+1])
 
    if len(list(set(pairs))) != len(pairs):
        for index, pair in enumerate(pairs):
            if pairs[index+2:].count(pair) > 0:
                two_pairs_found = True
    
    # rule 2 - contains two near-consecutive values
    near_consecutive_found = False
    pos = 0
    while pos < len(string) - 2:
        if string[pos] == string[pos+2]:
            near_consecutive_found = True
            break
        pos += 1
    
    if two_pairs_found and near_consecutive_found:
        return True
    return False

def solutions(puzzle_input):

    nice_strings = []
    naugthy_strings = []

    for string in puzzle_input:
        if solution(string):
            nice_strings.append(string)
        else:
            naugthy_strings.append(string)

    return len(nice_strings)

if __name__ == "__main__":
    puzzle_input = get_input()
    result = solutions(puzzle_input)
    print(result)
