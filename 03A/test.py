from solution import solution

tests = [
    [">", 2],
    ["^>v<", 4],
    ["^v^v^v^v^v", 2]
]

try:
    for (test_input, expected_result) in tests:
        result = solution([test_input])
        msg = "Input '%s' should result in value '%s' but the result was '%s' " % (test_input, expected_result, result)
        assert result == expected_result, msg
except AssertionError:
    print('Test failed: ' + msg)
finally:
    print('All tests finished')
