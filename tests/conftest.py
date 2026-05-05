import os
import pytest

#HARDWARE_AVAILABLE = os.path.exists('/dev/ttyUSB1')
HARDWARE_AVAILABLE = False

hardware = pytest.mark.skipif(
    not HARDWARE_AVAILABLE,
    reason="2B not plugged into /dev/TTYUSB1.  See conftest.py."
)
