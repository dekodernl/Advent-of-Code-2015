from solution import solution, process_input

tests = [
    [["turn on 0,0 through 999,999"], 1000*1000],
    [["toggle 0,0 through 999,0"], 1000],
    [["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"], (1000*1000)-4],
]

try:
    for (test_input, expected_result) in tests:
        instruction = process_input(test_input)
        result = solution(instruction)
        msg = "Input '%s' should result in value '%s' but the result was '%s' " % (test_input, expected_result, result)
        assert result == expected_result, msg
except AssertionError:
    print('Test failed: ' + msg)
finally:
    print('All tests finished')
