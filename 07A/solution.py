import re

def get_input():
    f = open('puzzle-input.txt', "r")
    instructions = []

    return f.readlines()


def solution(instructions):
    
    cmds = []
    for instruction in instructions:
        inst = instruction.strip().split(" -> ")
        output = inst.pop()
        cmd = (re.findall(r"(NOT|AND|OR|RSHIFT|LSHIFT)", inst[0]) or ["SET"]).pop()
        values = inst[0].replace(cmd + " ", "").split(" ")
        cmds.append((cmd, values, output)) 

    strints = [str(i) for i in range(0, 2**16)]

    wires = {}
    index = 0
    while len(cmds) > 0:
        cmd, values, output = cmds[index]
        set_values = []
        for val in values:
            if val in strints:
                set_values.append(int(val))
            elif val in wires.keys() and int(wires[val]) >= 0:
                set_values.append(wires[val])
        
        if len(values) == len(set_values):
            #print('cmd=%s, values=%s, output=%s' % (cmd, set_values, output) ) 
            if cmd == 'AND':
                wires[output] = set_values[0] & set_values[1]
            elif cmd == 'OR':
                wires[output] = set_values[0] | set_values[1]
            elif cmd == 'LSHIFT':
                wires[output] = set_values[0] << set_values[1]
            elif cmd == 'RSHIFT':
                wires[output] = set_values[0] >> set_values[1]
            elif cmd == 'NOT':
                wires[output] = (1 << 16) - 1 - set_values[0]
            elif cmd == 'SET':
                wires[output] = set_values[0]

            del cmds[index]
            index = 0
        else:
            index += 1


    return wires


if __name__ == "__main__":
    puzzle_input = get_input()
    result = solution(puzzle_input)
    print(result['a'])
