from estim2py import Estim2pyStatus

def test_constructor():
    bin = b'746:8:30:160:100:5:L:0:2.106\n'
    s = Estim2pyStatus.from_binary(bin)
    
    assert s.battery == 746
    assert s.a == 8
    assert s.b == 30
    assert s.c == 160
    assert s.d == 100
    assert s.mode == 5
    assert s.power == "L"
    assert s.linked == 0
    assert s.version == "2.106"

def test_get_scaled_level():
    bin = b'746:4:30:160:100:5:L:0:2.106\n'
    s = Estim2pyStatus.from_binary(bin)

    assert s.get_scaled_level("a") == 2
    assert s.get_scaled_level("b") == 15
    assert s.get_scaled_level("c") == 80
    assert s.get_scaled_level("d") == 50

def test_equal():
    bin = b'746:4:30:160:100:5:L:0:2.106\n'
    s = Estim2pyStatus.from_binary(bin)
    t = Estim2pyStatus.from_binary(bin)

def test_equal_different_battery_and_version():
    bin = b'746:4:30:160:100:5:L:0:2.106\n'
    s = Estim2pyStatus.from_binary(bin)

    same_bin = b'745:4:30:160:100:5:L:0:2.105\n'
    t = Estim2pyStatus.from_binary(same_bin)

    assert s == t

def test_not_equal():
    bin = b'746:4:30:160:100:5:L:0:2.106\n'
    s = Estim2pyStatus.from_binary(bin)

    diff_bin = b'745:0:30:160:100:5:L:0:2.105\n'
    t = Estim2pyStatus.from_binary(diff_bin)

    assert not s == t
    
