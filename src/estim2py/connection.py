import serial
import time
import logging
from .status import Estim2pyStatus

logger = logging.getLogger(__name__)

class Estim2pyConnection():
    """
    Connect to the Estim 2b box, and manage communication

    All method calls will return an Estim2pyStatus object.
    
    args:
    device - the serial device to connect with.

    keywords:
    timeout - Serial timeout, sent straight to pyserial
    delay - enforced delay.  May not be needed? If you're feeling spicy, set to 0 
    """

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
        """Returns a Estim2pyStatus object"""
        # May not be needed https://stackoverflow.com/questions/61596242/pyserial-when-should-i-use-flush#61602365
        if flush:  # "Fucking Voodoo Magic, Man"
            self.serial.flushInput()
            
        return self.__send("")

    def set_channel(self, channel, val):
        """Set's the channel to value val.

        Will throw a ValueError if:
        The channel is not a,b,c or d (upper or lowercase)
        The val is notan integer between 0-100 for A and B, 2-100 for C, or 1-100 for D

        args:
        channel (str): A or B for power channels, C for Speed, D for Feeling. (generally)
        val (int): 1-100 for A or B, 2-200 for C, 1-100 for D
        
        returns:
        Estim2pyStatus
        """
        channel = channel.upper()
        if channel not in ['A', 'B', 'C', 'D']: raise ValueError(f"channel argument must be A, B, C, D. was {channel!r}")
        if channel in ['A','B'] and (val > 100 or val < 0): raise ValueError(f"channel value out of range [0-100] was {val}")
        # More experimentation needed prolly
        if channel == 'C' and (val > 100 or val < 2): raise ValueError(f"channel value out of range [2-100] was {val}")
        if channel == 'D' and (val > 100 or val < 1): raise ValueError(f"channel value out of range [1-100] was {val}")

        return self.__send(channel+str(val))

    def reset(self):
        """Resets the box and returns Estim2pyStatus"""
        return self.__send("E")

    def low(self):
        """Sets the box to low power mode and returns Estim2pyStatus"""
        return self.__send("L")

    def high(self):
        """Sets the box to high power mode and returns Estim2pyStatus"""
        return self.__send("H")

    def link(self):
        """Enable's link mode and returns Estim2pyStatus.  Note, does not work on my box!"""
        return self.__send("J")

    def unlink(self):
        """Enable's link mode and returns Estim2pyStatus.  Note, does not work on my box!"""
        return self.__send("U")
    
    def kill(self):
        """Sets channels A and B to 0 and returns Estim2pyStatus"""
        return self.__send("K")

    def set_mode(self, mode_num):
        """Sets the mode to the numbered mode and returns Estim2pyStatus.

        Doesn't accept arguments over 100.  Note that my box only accepts up to 13.
        (I might need an update.)

        args:
        mode_num (int): mode number to set to.
        """
        if (mode_num < 0 or mode_num > self.MODE_MAX): raise ValueError("invalid mode number")
        return self.__send("M"+str(mode_num))
            
    def __receive(self):
        logger.debug(f"Sleeping for {self.delay}")
        time.sleep(self.delay)

        logger.debug("Getting all input until a \\n. If things are broken here, this is the problem.")
        # May be different line ending on windows!  Or version?

        input = self.serial.read_until(b"\n")
        logger.info(f"Received: {input}")
        return input

    def __send(self, out):
        command = out+"\r" # thank you STPIHKAL https://buttplug.io/stpihkal/protocols/estim-systems/
        logger.info(f"Sending command: {out}")
        self.serial.write(command.encode())
        # need a delay? between read and write? I don't know.
        return Estim2pyStatus.from_binary(self.__receive())
