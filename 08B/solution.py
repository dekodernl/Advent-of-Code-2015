import re

def get_input():
    with open('puzzle-input.txt') as f:
        lines = [r"{}".format(line.strip()) for line in f]

    return lines

def solution(instructions):
  
    lengths = []
    for i in instructions:
        codelen = len(i)
        chars = i[1:-1]
        chars = re.sub(r'\\', '\\\\\\\\', chars)
        chars = re.sub(r'\"', '\\\"', chars)
        chars = '"\\\"' + chars + '"\\\"'
        charlen = len(chars)
        lengths.append(charlen - codelen)

    return sum(lengths)

if __name__ == "__main__":
    puzzle_input = get_input()
    result = solution(puzzle_input)
    print(result)
