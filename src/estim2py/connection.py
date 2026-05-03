import serial
import time
from .status import Estim2pyStatus

class Estim2pyConnection():
    BAUD = 9600
    BYTESIZE = serial.EIGHTBITS
    PARITY = serial.PARITY_NONE
    STOPBITS = serial.STOPBITS_ONE

    MODE_MAX = 100
    
    def __init__(self, device, timeout=0.5, delay=0.05):
        self.delay = delay
        self.serial = serial.Serial(
            device,
            self.BAUD,
            timeout  = timeout,
            bytesize = self.BYTESIZE,
            parity   = self.PARITY,
            stopbits = self.STOPBITS)

    def get_status(self, flush=True):
        # May not be needed https://stackoverflow.com/questions/61596242/pyserial-when-should-i-use-flush#61602365
        if flush:  # "Fucking Voodoo Magic, Man"
            self.serial.flushInput()
            
        return self.__send("")

    def set_channel(self, channel, val):
        if channel not in ['A', 'B', 'C', 'D']: raise ValueError(f"channel argument must be A, B, C, D. was {channel!r}")
        if channel in ['A','B'] and (val > 100 or val < 0): raise ValueError(f"channel value out of range [0-100] was {val}")
        # More experimentation needed prolly
        if channel == 'C' and (val > 100 or val < 2): raise ValueError(f"channel value out of range [2-100] was {val}")
        if channel == 'D' and (val > 100 or val < 1): raise ValueError(f"channel value out of range [1-100] was {val}")

        return self.__send(channel+str(val))

    def reset(self):
        return self.__send("E")

    def low(self):
        return self.__send("L")

    def high(self):
        return self.__send("H")

    def link(self):
        return self.__send("J")

    def unlink(self):
        return self.__send("U")
    
    def kill(self):
        return self.__send("K")

    def set_mode(self, mode_num):
        if (mode_num < 0 or mode_num > self.MODE_MAX): raise ValueError("invalid mode number")
        return self.__send("M"+str(mode_num))
            
    def __receive(self):
        time.sleep(self.delay)

        # May be different line ending on windows!  Or version?
        return self.serial.read_until(b"\n")

    def __send(self, out):
        command = out+"\r" # thank you STPIHKAL https://buttplug.io/stpihkal/protocols/estim-systems/
        self.serial.write(command.encode())
        # need a delay? between read and write? I don't know.
        return Estim2pyStatus.from_binary(self.__receive())
