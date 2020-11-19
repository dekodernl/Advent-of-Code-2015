from solution import solution

def get_input():
    with open('test-data.txt') as f:
        lines = [r"{}".format(line.strip()) for line in f]

    return lines


try:
    test_input = get_input()    
    result = solution(test_input)
    expected_result = 12
    msg = "Input '%s' should result in value '%s' but the result was '%s' " % (test_input, expected_result, result)
    assert result == expected_result, msg
except AssertionError:
    print('Test failed: ' + msg)
finally:
    print('End of testing')
