import hashlib

def get_input():
    return "yzbqklnj"

def solution(puzzle_input):
    number = 1
    while True:
        md5 = hashlib.md5( ( puzzle_input + str(number) ).encode() ).hexdigest()
        print(str(number) + (" " * 20), end="\r")
        if md5[:6] == "000000":
            return number
        number += 1

if __name__ == "__main__":
    puzzle_input = get_input()
    result = solution(puzzle_input)
    print(result)
