from .__version__ import __version__
from .status import Estim2pyStatus
from .connection import Estim2pyConnection


# NOTE!  Next refactor, override send and recieve, call super, and then set status
class Estim2pySimulatedConnection(Estim2pyConnection):
    """
    This is a sumulated 2B box, so you don't always have to plug a box in to write code.
    It should behave exactly like the real box.

    If it doesn't... that's a bug!

    The interface is exactly like Estim2pyConnection.
    """
    def __init__(self):
        self.serial = None
        self.reset_status()

    def reset_status(self):
        """Manually reset the status to the default state."""
        self.status = Estim2pyStatus(230,0,0,100,100,0,"L",0,__version__)
            
    def get_status(self):
        return self.status

    def set_channel(self, channel, val):
        setattr(self.status, channel.lower(), val*2)
        return self.status

    def reset(self):
        self.reset_status()
        return self.status

    def low(self):
        self.kill()
        self.status.power = "L"
        return self.status

    def high(self):
        self.kill()
        self.status.power = "H"
        return self.status

    def link(self):
        self.status.linked = 1
        return self.status

    def unlink(self):
        self.status.linked = 0
        return self.status

    def kill(self):
        self.set_channel("A",0)
        self.set_channel("B",0)
        return self.status

    def set_mode(self, mode_num):
        power = self.status.power
        linked = self.status.linked

        self.reset_status()
        
        self.status.mode = mode_num
        self.status.power = power
        self.status.linked = linked

        return self.status
