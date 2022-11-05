from payment import *
#test
def test(a, b):
    c = calculate(a,b)
    test_c = a+b

    assert c == test_c

test(10,20)
test(1,15)
test(40,150)
test(60,80)
