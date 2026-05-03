from estim2py import Estim2pyModes

def test_constructor():
    m = Estim2pyModes.get_mode(0)
    assert m.mid == 0
    assert m.name == "pulse"
    assert m.param_a == "pulse speed"
    assert m.param_b == "pulse feel"
    assert m.notes == "Pulsing on and off"
    
