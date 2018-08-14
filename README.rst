Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-tca9548a/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/tca9548a/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.org/adafruit/Adafruit_CircuitPython_TCA9548A.svg?branch=master
    :target: https://travis-ci.org/adafruit/Adafruit_CircuitPython_TCA9548A
    :alt: Build Status

CircuitPython driver for the TCA9548A I2C Multiplexer.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block :: python

    # This example shows using two TSL2491 light sensors attached to TCA9548A channels 0 and 1.
    # Use with other I2C sensors would be similar.
    import time
    import board
    import busio
    import adafruit_tsl2591
    import adafruit_tca9548a

    # Create I2C bus as normal
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the TCA9548A object and give it the I2C bus
    tca = adafruit_tca9548a.TCA9548A(i2c)

    # For each sensor, create it using the TCA9548A channel instead of the I2C object
    tsl1 = adafruit_tsl2591.TSL2591(tca[0])
    tsl2 = adafruit_tsl2591.TSL2591(tca[1])

    # Loop and profit!
    while True:
        print(tsl1.lux, tsl2.lux)
        time.sleep(0.1)


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_TCA9548A/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Zip release files
-----------------

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-tca9548a --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
