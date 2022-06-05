# SPDX-FileCopyrightText: 2018 Carter Nelson for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_tca9548a`
====================================================

CircuitPython driver for the TCA9548A I2C Multiplexer.

* Author(s): Carter Nelson

Implementation Notes
--------------------

**Hardware:**

* `TCA9548A I2C Multiplexer
  <https://www.adafruit.com/product/2717>`_ (Product ID: 2717)


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

* Adafruit's Bus Device library:
  https://github.com/adafruit/Adafruit_CircuitPython_BusDevice

"""

from micropython import const

_DEFAULT_ADDRESS = const(0x70)

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A.git"


class TCA9548A_Channel:
    """Helper class to represent an output channel on the TCA9548A and take care
    of the necessary I2C commands for channel switching. This class needs to
    behave like an I2CDevice."""

    def __init__(self, tca, channel):
        self.tca = tca
        self.channel_switch = bytearray([1 << channel])

    def try_lock(self):
        """Pass through for try_lock."""
        while not self.tca.i2c.try_lock():
            pass
        self.tca.i2c.writeto(self.tca.address, self.channel_switch)
        return True

    def unlock(self):
        """Pass through for unlock."""
        self.tca.i2c.writeto(self.tca.address, b"\x00")
        return self.tca.i2c.unlock()

    def readfrom_into(self, address, buffer, **kwargs):
        """Pass through for readfrom_into."""
        if address == self.tca.address:
            raise ValueError("Device address must be different than TCA9548A address.")
        self.tca.i2c.writeto(self.tca.address, self.channel_switch)
        return self.tca.i2c.readfrom_into(address, buffer, **kwargs)

    def writeto(self, address, buffer, **kwargs):
        """Pass through for writeto."""
        if address == self.tca.address:
            raise ValueError("Device address must be different than TCA9548A address.")
        self.tca.i2c.writeto(self.tca.address, self.channel_switch)
        return self.tca.i2c.writeto(address, buffer, **kwargs)

    def writeto_then_readfrom(self, address, buffer_out, buffer_in, **kwargs):
        """Pass through for writeto_then_readfrom."""
        # In linux, at least, this is a special kernel function call
        if address == self.tca.address:
            raise ValueError("Device address must be different than TCA9548A address.")
        self.tca.i2c.writeto(self.tca.address, self.channel_switch)
        return self.tca.i2c.writeto_then_readfrom(
            address, buffer_out, buffer_in, **kwargs
        )

    def scan(self):
        """Perform an I2C Device Scan"""
        return self.tca.i2c.scan()


class TCA9548A:
    """Class which provides interface to TCA9548A I2C multiplexer."""

    def __init__(self, i2c, address=_DEFAULT_ADDRESS):
        self.i2c = i2c
        self.address = address
        self.channels = [None] * 8

    def __len__(self):
        return 8

    def __getitem__(self, key):
        if not 0 <= key <= 7:
            raise IndexError("Channel must be an integer in the range: 0-7.")
        if self.channels[key] is None:
            self.channels[key] = TCA9548A_Channel(self, key)
        return self.channels[key]
