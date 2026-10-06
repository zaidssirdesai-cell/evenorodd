from oddeven import evenorodd

def test_1():
    assert evenorodd(3) == odd

def test_2():
    assert evenorodd(10) == even

def test_3():
    assert evenorodd(300) == even