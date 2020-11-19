import re
import itertools

def get_input():
    with open('puzzle-input.txt') as f:
        lines = [r"{}".format(line.strip()) for line in f]
    return lines


def solution(instructions):
   
    locations = list(set(re.findall(r'([A-Z]\w+)', " ".join(instructions))))

    pairs = []
    for i in instructions:
        dist = re.findall(r'([A-Z]\w+)(?:\sto\s)([A-Z]\w+)(?:\s=\s)(\d{1,})' ,i)[0]
        pairs.append(dict(src=dist[0], dest=dist[1], dist=int(dist[2])))
        pairs.append(dict(src=dist[1], dest=dist[0], dist=int(dist[2])))

    highest = 0
    for c in itertools.permutations(range(len(locations)), len(locations)):
        dist = 0
        for i in range(0, len(c)-1):
            dist += [p['dist'] for p in pairs \
                     if p['src'] == locations[c[i]] \
                     and p['dest'] == locations[c[i+1]]][0]
        if dist > highest:
            highest = dist

    return highest


if __name__ == "__main__":
    puzzle_input = get_input()
    result = solution(puzzle_input)
    print(result)
