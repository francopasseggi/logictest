import pytest

from fizzbuzz import fizzbuzz
from fibonacci import fib
from word_repetitions import count_words

def test_fizzbuzz():
    pytest.raises(ValueError, fizzbuzz, -1)
    pytest.raises(TypeError, fizzbuzz, 1.5)

    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(15) == "fizz buzz"
    assert fizzbuzz(4) == 4


def test_fibonacci():
    pytest.raises(ValueError, fib, -1)
    pytest.raises(TypeError, fib, 1.5)

    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2

    assert fib(10) == 55


def test_word_repetitions():
    sentence = "Hi how are things? How are you? Are you a developer? I am also a developer"
    frequencies = count_words(sentence)

    assert frequencies["hi"] == 1
    assert frequencies["how"] == 2
    assert frequencies["are"] == 3
    assert frequencies["things"] == 1
    assert frequencies["you"] == 2
    assert frequencies["a"] == 2
    assert frequencies["developer"] == 2
    assert frequencies["i"] == 1
    assert frequencies["am"] == 1
    assert frequencies["also"] == 1

    # raise key error if word not in dictionary
    pytest.raises(KeyError, frequencies.__getitem__, "hello")