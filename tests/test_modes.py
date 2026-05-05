from estim2py import Estim2pyMode

def test_constructor():
    m = Estim2pyMode.get_mode(0)
    assert m.mid == 0
    assert m.name == "pulse"
    assert m.param_a == "pulse speed"
    assert m.param_b == "pulse feel"
    assert m.notes == "Pulsing on and off"

def test_mode_id_names():
    modes = Estim2pyMode.id_names()

    assert modes[0] == "pulse"
    assert modes[5] == "wave"
    assert modes[8] == "milk"
    assert modes[13] == "training"
