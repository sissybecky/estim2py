import pytest
from estim2py import Estim2pyStatus
from estim2py import Estim2pyConnection
from estim2py import Estim2pySimulatedConnection

def test_constructor(default_status):
    s = Estim2pySimulatedConnection()
    assert isinstance(s, Estim2pyConnection)

    assert s.get_status() == default_status
        
def test_set_and_get(driver, default_status, changed_status):
    assert driver.get_status() == default_status
    assert driver.change_all() == changed_status
    
def test_kill(driver, default_status, changed_status, changed_then_kill):
    assert driver.get_status() == default_status
    assert driver.change_all() == changed_status
    
    assert driver.target.kill() == changed_then_kill
    
def test_mode(driver, default_status, changed_status, changed_then_mode):
    assert driver.get_status() == default_status
    assert driver.change_all() == changed_status
    assert driver.target.set_mode(5) == changed_then_mode
    
def test_reset(driver, default_status, changed_status):
    assert driver.get_status() == default_status
    assert driver.change_all() == changed_status
    driver.target.reset()
    assert driver.get_status() == default_status
    
@pytest.fixture
def default_status():
    return Estim2pyStatus.from_binary(b"320:0:0:100:100:0:L:0:0.0.1\n")

@pytest.fixture
def changed_status():
    return Estim2pyStatus.from_binary(b"320:2:4:8:24:0:H:1:0.0.1\n")

@pytest.fixture
def changed_then_mode():
    return Estim2pyStatus.from_binary(b"320:0:0:100:100:5:H:1:0.0.1\n")

@pytest.fixture
def changed_then_power():
    return Estim2pyStatus.from_binary(b"320:0:0:40:60:0:H:1:0.0.1\n")

@pytest.fixture
def changed_then_kill():
    return Estim2pyStatus.from_binary(b"320:0:0:8:24:0:H:1:0.0.1\n")

@pytest.fixture
def driver():
    return BoxDriver()
    
class BoxDriver():
    def __init__(self):
        self.target = Estim2pySimulatedConnection()

    def get_status(self):
        return self.target.get_status()
        
    def change_all(self):
        self.set_high()
        self.set_link()
        self.set_channels()

        return self.get_status()
    
    def set_high(self):
        return self.target.high()

    def set_link(self):
        return self.target.link()
        
    def set_channels(self):    
        self.target.set_channel('A',1)
        self.target.set_channel('B',2)
        self.target.set_channel('C',4)
        return self.target.set_channel('D',12)
        
