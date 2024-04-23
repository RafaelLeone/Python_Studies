from old.find_two_highest_numbers import find_higher

def test_find_higher():
    result = find_higher([-10, 80, 100, 80, 100, 80, 100, 90, 90, 90, 100, 80, 100, 100, 90])
    assert result == {100: 6, 90: 4}

def test_find_higher_with_same_number():
    result = find_higher([90, 90, 90, 90])
    assert result == {90: 4}

def test_find_higher_with_negative():
    result = find_higher([-10, -180, -100, -80, -100, -80, -100, -90, -90, -90, -100, -80])
    assert result == {-10: 1, -80: 3}
