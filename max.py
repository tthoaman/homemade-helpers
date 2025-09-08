def max(my_collection):
    pass

def test_max_empty_list():
    assert max([]) == None

def test_max_single_list():
    assert max([1]) == 1

def test_max_many_list():
    assert max([4, 5, 8, 3, 9]) == 9

def max_tests():
    test_max_empty_list()
    test_max_single_list()
    test_max_many_list()
    print("All max tests passing.")