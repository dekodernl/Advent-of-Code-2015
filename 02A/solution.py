def get_input():
    f = open('puzzle-input.txt', "r")
    lines = f.readlines()
    return [ [ int(l), int(w), int(h) ] for l, w, h in [ lin.replace("\n", "").split("x") for lin in lines] ]

def solution(puzzle_input):
    total_wrapping_paper = 0

    for (l, w, h) in puzzle_input:
        surfaces = [2*l*w, 2*w*h, 2*h*l]
        total_wrapping_paper += sum(surfaces) + min(l*w,w*h,h*l)
   
    return total_wrapping_paper

if __name__ == "__main__":
    puzzle_input = get_input()
    result = solution(puzzle_input)
    print(result)
