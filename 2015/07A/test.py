from solution import solution

instructions = [
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i"
]

assertions = {
    'd': 72,
    'e': 507,
    'f': 492,
    'g': 114,
    'h': 65412,
    'i': 65079,
    'x': 123,
    'y': 456
}

try:
    wires = solution(instructions)

    for wire in wires:
        msg = "Key '%s' should have value '%s' but has value '%s'" % (wire, assertions[wire], wires[wire])
        assert wires[wire] == assertions[wire], msg
except AssertionError:
    print('Test failed: ' + msg)
finally:
    print('All tests finished')
