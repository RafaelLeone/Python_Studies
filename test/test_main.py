from main import concatenate_lists, order_list, find_median


def test_concatenate_lists():
    result = concatenate_lists([1, 2, 3], [4, 5, 6])
    assert result == [1, 2, 3, 4, 5, 6]

def test_order_list():
    result = order_list([3, 1, 2, 5, 4])
    assert result == [1, 2, 3, 4, 5]

def test_find_median_odd():
    result = find_median([1, 2, 3, 4, 5])
    assert result == 3

def test_find_median_even():
    result = find_median([1, 2, 3, 4])
    assert result == 2.5
