import operator
def get_input():
    f = open('puzzle-input.txt', "r")
    return f.readline().strip()

def solution(puzzle_input):
    santa_location = (0, 0)
    robo_location  = (0, 0)
    
    houses = dict({ (0, 0) : 2 })

    moves = []
    actions = {
        "^" : (-1,  0),
        ">" : ( 0,  1),
        "v" : ( 1,  0),
        "<" : ( 0, -1)
    }

    for char in puzzle_input:
        moves.append(actions[char])

    for i, move in enumerate(moves):
        if i % 2 == 0:
            santa_location = tuple(x + y for x, y in zip(santa_location, move))
            if santa_location not in houses.keys():
                houses[santa_location] = 0
            houses[santa_location] += 1

        else:
            robo_location = tuple(x + y for x, y in zip(robo_location, move))
            if robo_location not in houses.keys():
                houses[robo_location] = 0
            houses[robo_location] += 1
    
    return len(houses.keys())


if __name__ == "__main__":
    puzzle_input = get_input()
    result = solution(puzzle_input)
    print(result)
