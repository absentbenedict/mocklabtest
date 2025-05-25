import mocklab as ml

def test_is_palindrome_true():
    assert ml.is_palindrome("madam") == 1

def test_is_palindrome_false():
    assert ml.is_palindrome("apple") == 0

def test_is_palindrome_case_insensitive():
    assert ml.is_palindrome("RaceCar") == 1