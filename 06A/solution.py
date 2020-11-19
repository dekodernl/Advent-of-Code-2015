import re

def process_input(puzzle_input):
    instructions = []
    for line in puzzle_input:
        pattern = r"(toggle|turn off|turn on)(?:\s)"\
            "(\d{1,3})\,(\d{1,3})(?:\sthrough\s)(\d{1,3})\,(\d{1,3})"
        m = re.findall(pattern, line)
        print(m)
        instructions.append((m[0][0], [int(i) for i in m[0][1:]]))
    return instructions

def get_input():
    f = open('puzzle-input.txt', "r")
    instructions = []

    return f.readlines()

def print_grid(grid, size):
    for y in range(0,size):
        for x in range(0, size):
            print(grid[y][x], end=" ")
        print("\r")

def solution(instructions):
    size = 1000
    grid = [[0 for x in range(size)] for x in range(size)]

    for action, coordinates in instructions:
        ax, ay, bx, by = coordinates
        for y in range(ay, by+1):
            for x in range(ax, bx+1):
                if action == 'toggle':
                    if grid[y][x] == 1:
                        grid[y][x] = 0
                    else:
                        grid[y][x] = 1
                elif action == 'turn on':
                    grid[y][x] = 1
                else:
                    grid[y][x] = 0


    #print_grid(grid, size)

    lights_shining = sum(grid, [])

    return lights_shining.count(1)

if __name__ == "__main__":
    puzzle_input = get_input()
    instructions = process_input(puzzle_input)
    result = solution(instructions)
    print(result)
