from estim2py import Estim2pyStatus
import pytest

def test_constructor(a_status):    
    assert a_status.battery == 746
    assert a_status.a == 8
    assert a_status.b == 30
    assert a_status.c == 160
    assert a_status.d == 100
    assert a_status.mode == 5
    assert a_status.power == "L"
    assert a_status.linked == 0
    assert a_status.version == "2.106"

def test_get_mode():
    bin = b'746:4:30:160:100:5:L:0:2.106\n'
    s = Estim2pyStatus.from_binary(bin)

    m = s.get_mode()
    assert m.mid == 5
    
def test_get_channel():
    bin = b'746:4:30:160:100:5:L:0:2.106\n'
    s = Estim2pyStatus.from_binary(bin)

    assert s.get_channel("a") == 2
    assert s.get_channel("b") == 15
    assert s.get_channel("c") == 80
    assert s.get_channel("d") == 50

def test_get_channel_handles_uppercase():
    bin = b'746:4:30:160:100:5:L:0:2.106\n'
    s = Estim2pyStatus.from_binary(bin)

    assert s.get_channel("A") == 2

def test_get_channel_errors_invalid(a_status):
    with pytest.raises(ValueError):
        assert a_status.get_channel("E")
    
    
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

def test_not_equal_type(a_status):
    assert not a_status == None
    
def items():
    bin = b'746:4:30:160:100:5:L:0:2.106\n'
    s = Estim2pyStatus.from_binary(bin)

    expected = [
        ("battery",745),
        ("a",4),
        ("b",30),
        ("c",160),
        ("d",100),
        ("mode",5),
        ("power","L"),
        ("linked",0),
        ("version","2.106")]
    
    assert s.as_items() == expected
    
@pytest.fixture
def a_status():
    return Estim2pyStatus.from_binary(b'746:8:30:160:100:5:L:0:2.106\n')
