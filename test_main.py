from main import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("racecar") == True

def test_non_palindrome():
    assert is_palindrome("hello") == False

def test_sentence_palindrome():
    assert is_palindrome("Never odd or even") == True