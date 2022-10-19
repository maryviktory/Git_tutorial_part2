from  new_feature_file import *
def test(a, b):
    c = calculate(a,b)
    test_c = a/b

    assert c == test_c

test(10,20)
