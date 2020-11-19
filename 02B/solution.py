def get_input():
    f = open('puzzle-input.txt', "r")
    lines = f.readlines()
    return [ [ int(l), int(w), int(h) ] for l, w, h in [ lin.replace("\n", "").split("x") for lin in lines] ]

def solution(puzzle_input):
    total_feet_of_ribbon = 0

    for (l, w, h) in puzzle_input:
        total_feet_of_ribbon += (2 * l) + (2 * w) + (2 * h) - (2 * max(l, w, h)) + (l * w * h)
   
    return total_feet_of_ribbon

if __name__ == "__main__":
    puzzle_input = get_input()
    result = solution(puzzle_input)
    print(result)
