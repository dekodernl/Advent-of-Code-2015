def get_input():
    f = open('puzzle-input.txt', "r")
    return f.readline()

def solution(puzzle_input):
    return puzzle_input.count("(") - puzzle_input.count(")")

if __name__ == "__main__":
    puzzle_input = get_input()
    result = solution(puzzle_input)
    print(result)
