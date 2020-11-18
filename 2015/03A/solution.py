def get_input():
    f = open('puzzle-input.txt', "r")
    return f.readline()

def solution(puzzle_input):
    x, y = 0, 0
    
    houses = dict({ (0,0) : 1 })

    puzzle_input = str(puzzle_input)\
        .replace("^", "N")\
        .replace(">", "E")\
        .replace("v", "S")\
        .replace("<", "W")

    for move in puzzle_input:
        
        if move == 'N':
            y += 1
        elif move == 'E':
            x += 1
        elif move == 'S':
            y -= 1
        elif move == 'W':
            x -= 1
        
        if (x,y) in houses.keys():
            houses[(x,y)] += 1
        else:
            houses[(x,y)] = 1

    return len(houses)

if __name__ == "__main__":
    puzzle_input = get_input()
    result = solution(puzzle_input)
    print(result)
