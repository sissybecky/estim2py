class Estim2pyStatus:

    def __init__(self, battery, a, b, c, d, mode, power, linked, version):
        self.battery = battery
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.mode = mode
        self.power = power
        self.linked = linked
        self.version = version

    def get_scaled_level(self, param):
        return getattr(self, param) // 2

    def high_power(self):
        return self.power == "H"
    
    def low_power(self):
        return self.power == "L"
    
    def linked(self):
        return self.linked == 1
        
    def unlinked(self):
        return self.linked == 0

    def get_mode(self):
        return Estim2PyModes.get_mode(self.mode)

    def __eq__(self, other):
        return (self.a == other.a) and\
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

     
