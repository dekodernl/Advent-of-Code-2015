from solution import looksay 

tests = [
    [1, 11],
    [11, 21],
    [21, 1211],
    [1211, 111221],
    [111221, 312211]
]

try:
    for (test_input, expected_result) in tests:
        result = int(looksay(test_input))
        msg = "Input '%s' should result in value '%s' but value is '%s'." % (test_input, expected_result, result)
        assert result == expected_result, msg
except AssertionError:
    print('Test failed: ' + msg)
finally:
    print('All tests finished')
