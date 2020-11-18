from solution import solution

tests = [
    ["(())", 0],
    ["()()", 0],
    ["(((", 3],
    ["(()(()(", 3],
    ["))(((((",3],
    ["())", -1],
    ["))(", -1],
    [")))", -3],
    [")())())", -3]
]

try:
    for (test_input, expected_result) in tests:
        msg = "Input '%s' should result in value '%s'" % (test_input, expected_result)
        assert solution(test_input) == expected_result, msg
except AssertionError:
    print('Test failed: ' + msg)
finally:
    print('All tests finished')
