from .modes import Estim2pyMode

class Estim2pyStatus:
    """An object that reports back the status of the Estim Box.

    Object members are direct from the serial port.  Object methods relate closer to what the box displays and return useful python objects.

    i.e. status.a will return 200 at max power, but get_channel('a') will return 100.
    """
    def __init__(self, battery, a, b, c, d, mode, power, linked, version):
        """Not meant for instantiation directly.  But you can if you want I guess?"""
        self.battery = battery
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.mode = mode
        self.power = power
        self.linked = linked
        self.version = version

    def get_channel(self, channel):
        """Returns the value of the channel as reported by the box.

        Channel must be a,b,c or d (upper or lower).
        The value is half of what's reported on the serial port, and is what is displayed on the LCD.

        This value is compatible with Estim2pyConnection.set_channel().
        """
        if channel.lower() not in ['a','b','c','d']: raise ValueError(f"channel argument must be A, B, C, D. was {channel!r}")
        return getattr(self, channel.lower()) // 2

    def high_power(self):
        """Returns True if the box is in high power mode, False otherwise."""
        return self.power == "H"
    
    def low_power(self):
        """Returns True if the box is in low power mode, False otherwise."""
        return self.power == "L"
    
    def linked(self):
        """Return True if the box is in linked mode, False otherwise."""
        return self.linked == 1
        
    def unlinked(self):
        """Returns True if the box is in unlinked mode, False otherwise."""
        return self.linked == 0

    def get_mode(self):
        """Returns an Estim2pyMode representing the current mode.

        See Estim2pyMode for more information."""
        return Estim2pyMode.get_mode(self.mode)

    def as_items(self):
        """Returns an items-like represtation of the status.

        It's 'items-like' in that you can use it for iteration, but modifying
        the values of the tuples inside the dictionary does nothing.

        NOTE, this is the raw values from the serial port.
        """
        return [("battery",self.battery),
                ("a",self.a),
                ("b",self.b),
                ("c",self.c),
                ("d",self.d),
                ("mode",self.mode),
                ("power",self.power),
                ("linked",self.linked),
                ("version",self.version)]
    
    def __eq__(self, other):
        """Perform an equality check.

        This means you can do Estim2pyStatus == Estim2pyStatus and it will do the right thing!

        It ignores battery and version information as "incidental".
        """
        return isinstance(other, Estim2pyStatus) and\
            (self.a == other.a) and\
            (self.b == other.b) and\
            (self.c == other.c) and\
            (self.d == other.d) and\
            (self.mode == other.mode) and\
            (self.power == other.power) and\
            (self.linked == other.linked)

    def __repr__(self):
        return f"{type(self).__name__}({self.battery=},{self.a=},{self.b=},{self.c=},{self.d=},{self.mode=},{self.power=},{self.linked=},{self.version})"
    
    @staticmethod
    def from_binary(bin):
        """Return an Estim2pyStatus object form a binary string.

        This is mostly internal, but may be useful in some circumstances.  Check unit tests."""
        string = bin.decode().strip()
        if not ":" in string:
            ValueError('could not find %s in %s' % (":",string))

        vals = string.split(":")
        return Estim2pyStatus(int(vals[0]),\
                              int(vals[1]),\
                              int(vals[2]),\
                              int(vals[3]),\
                              int(vals[4]),\
                              int(vals[5]),\
                              str(vals[6]),\
                              int(vals[7]),\
                              str(vals[8]))

     
