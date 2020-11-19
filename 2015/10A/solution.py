from itertools import groupby

def get_input():
    f = open('puzzle-input.txt', "r")
    instructions = []

    return f.readlines()

def looksay(number):
    return ''.join( str(len(list(g))) + k for k, g in groupby(str(number)))

def solution(puzzle_input):

    output = puzzle_input

    for i in range(40):
        output = looksay(output)
    
    return len(str(output))


if __name__ == "__main__":
    puzzle_input = 1321131112
    result = solution(puzzle_input)
    print(result)
