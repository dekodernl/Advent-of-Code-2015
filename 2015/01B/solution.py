def get_input():
    f = open('puzzle-input.txt', "r")
    return f.readline()

def solution(puzzle_input):
    floor = 0
    position = 0
    while floor != -1:
        if puzzle_input[position] == "(":
            floor += 1
        else:
            floor -= 1
        position += 1
        if floor == -1:
            return position

    return 0

if __name__ == "__main__":
    puzzle_input = get_input()
    result = solution(puzzle_input)
    print(result)
