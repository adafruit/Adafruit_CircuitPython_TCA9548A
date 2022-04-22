Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-tca9548a/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/tca9548a/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_Bundle/blob/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A/actions/
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black


CircuitPython driver for the TCA9548A I2C Multiplexer.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-tca9548a/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-tca9548a

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-tca9548a

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-tca9548a

Usage Example
=============

.. code-block :: python

    # This example shows using TCA9548A to perform a simple scan for connected devices
    import board
    import adafruit_tca9548a

    # Create I2C bus as normal
    i2c = board.I2C()  # uses board.SCL and board.SDA

    # Create the TCA9548A object and give it the I2C bus
    tca = adafruit_tca9548a.TCA9548A(i2c)

    for channel in range(8):
        if tca[channel].try_lock():
            print("Channel {}:".format(channel), end="")
            addresses = tca[channel].scan()
            print([hex(address) for address in addresses if address != 0x70])
            tca[channel].unlock()


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/tca9548a/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
