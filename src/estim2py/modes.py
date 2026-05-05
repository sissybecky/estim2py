class Estim2pyMode:
    """A class representing a mode for the Estim 2b.

    Construct with Estim2pyMode.get_mode(int).  That will return the relevant mode by integer id.
    """
    
    modes = {
        0: { "name":"pulse",     "param_a": "pulse speed", "param_b": "pulse feel", "notes": "Pulsing on and off" },
        1: { "name":"bounce",    "param_a": "pulse speed", "param_b": "pulse feel", "notes": "Pulsing alternatively" },
        2: { "name":"continious","param_a": "pulse feel", "param_b": None,          "notes": "Both channels always on" },
        3: { "name":"asplit",    "param_a": "pulse speed", "param_b": "pulse feel", "notes": "A Pulse B Continious" },
        4: { "name":"bsplit",    "param_a": "pulse speed", "param_b": "pulse feel", "notes": "B Pulse A Continious" },
        5: { "name":"wave",      "param_a": "speed of increase",            "param_b": "wave feel",   "notes": "Output increases to power, then to 0" },
        6: { "name":"waterfall", "param_a": "speed of increase / decrease", "param_b": "waterfall feel", "notes": "Output to power, then back down" },
        7: { "name":"squeeze",   "param_a": "pulse speed", "param_b": "feel", "notes": "Pulse rate increases and then drops to slow" },
        8: { "name":"milk",      "param_a": "pulse speed", "param_b": "feel", "notes": "Pulse rate increases and then drops to slow, b channel alternates" },
        9: { "name":"throb",     "param_a": "feel range", "param_b": None, "notes": "Continious, with the feel increasing to range and dropping to 0" },
        10: { "name":"thrust",   "param_a": "feel range", "param_b": None, "notes": "Continious, with the feel increasing to range and decreasing" },
        11: { "name":"random",   "param_a": "random range", "param_b": "pulse feel", "notes": "Random Levels" },
        12: { "name":"step",     "param_a": "step delay", "param_b": "pulse feel", "notes": "Builds towards a power level slowly" },
        13: { "name":"training", "param_a": "jump delay", "param_b": "pulse feel", "notes": "Jumps to the power level quickly" }
    }
    """List of modes that this class knows about. Access directly if you like!"""
    
    def __init__(self, mid, name, param_a, param_b, notes):
        self.mid = mid
        """numeric id of the mode."""
        self.name = name
        """Short name of the mode."""
        self.param_a = param_a
        """What channel C modifies."""
        self.param_b = param_b
        """What channel D modifies, or None if not applicable"""
        self.notes = notes
        """A real short description of the mode."""
        
    @staticmethod
    def get_mode(mid):
        """Returns the mode based on the integer id.""" 
        m = Estim2pyMode.modes[mid]
        return Estim2pyMode(mid, m["name"], m["param_a"], m["param_b"], m["notes"])

    @classmethod
    def id_names(__class__):
        """returns a dictionary of {modeid: name, ...}

        ie. {0: "pulse", 1: "bounce", ...}
        """ 
        return {m: v['name'] for m, v in __class__.modes.items()}


