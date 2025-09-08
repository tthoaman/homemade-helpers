def min(my_collection):
    pass
    

def test_min_empty_list():
    assert min([]) == None

def test_min_single_list():
    assert min([1]) == 1

def test_min_many_list():
    assert min([4, 5, 8, 3, 9]) == 3

def min_tests():
    test_min_empty_list()
    test_min_single_list()
    test_min_many_list()
    print("All min tests passing.")