from itertools import permutations, combinations

"""
attendee_happiness = {
    'Alice': {
        'Bob': 54,
        'Carol': -79,
        'David': -2
    },
    'Bob': {
        'Alice': 83,
        'Carol': -7,
        'David': -63
    },
    'Carol': {
        'Alice': -62,
        'Bob': 60,
        'David': 55
    }, 
    'David':{
        'Alice': 46,
        'Bob': -7,
        'Carol': 41
    }
}
"""

attendee_happiness = {
    "Alice": {
        "Bas": 0,
        "Bob": -57,
        "Carol": -62,
        "David": -75,
        "Eric": 71,
        "Frank": -22,
        "George": -23,
        "Mallory": -76
    },
    "Bob": {
        "Alice": -14,
        "Bas": 0,
        "Carol": 48,
        "David": 89,
        "Eric": 86,
        "Frank": -2,
        "George": 27,
        "Mallory": 19
    },
    "Carol": {
        "Alice": 37,
        "Bob": 45,
        "Bas": 0,
        "David": 24,
        "Eric": 5,
        "Frank": -68,
        "George": -25,
        "Mallory": 30
    },
    "David": {
        "Alice": -51,
        "Bob": 34,
        "Carol": 99,
        "Bas": 0,
        "Eric": 91,
        "Frank": -38,
        "George": 60,
        "Mallory": -63
    },
    "Eric": {
        "Alice": 23,
        "Bob": -69,
        "Carol": -33,
        "David": -47,
        "Bas": 0,
        "Frank": 75,
        "George": 82,
        "Mallory": 13
    },
    "Frank": {
        "Alice": 77,
        "Bob": 27,
        "Carol": -87,
        "David": 74,
        "Eric": -41,
        "Bas": 0,
        "George": -99,
        "Mallory": 26
    },
    "George": {
        "Alice": -63,
        "Bob": -51,
        "Carol": -60,
        "David": 30,
        "Eric": -100,
        "Frank": -63,
        "Bas": 0,
        "Mallory": 57
    },
    "Mallory": {
        "Alice": -71,
        "Bob": -28,
        "Carol": -10,
        "David": 44,
        "Eric": 22,
        "Frank": 79,
        "George": -16,
        "Bas": 0
    },
    "Bas": {
        "Alice": 0,
        "Bob": 0,
        "Carol": 0,
        "David": 0,
        "Eric": 0,
        "Frank": 0,
        "George": 0,
        "Mallory": 0
    }
}

def solution():

    attendees = list(attendee_happiness.keys())
    highest = (2 ** 16) * -1
    al = len(attendees)
    for seating in permutations(range(0, al), al):
        happiness = []
        for chair in seating:
            left = attendees[seating[(chair - 1) % al]]
            me = attendees[seating[chair]]
            right = attendees[seating[(chair + 1) % al]]

            happiness.append(attendee_happiness[me][left])
            happiness.append(attendee_happiness[me][right])

        total = sum(happiness)

        if total > highest:
            highest = total
            highest_happiness = happiness
            highest_seating = [attendees[chair] for chair in seating]

    print(highest, highest_happiness)
    print(highest_seating)

    return highest


if __name__ == "__main__":
    result = solution()
    print(result)
