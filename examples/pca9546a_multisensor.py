# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example shows using two TSL2491 light sensors attached to PCA9546A channels 0 and 1.
# Use with other I2C sensors would be similar.
import time

import adafruit_tsl2591
import board

import adafruit_tca9548a

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Create the PCA9546A object and give it the I2C bus
mux = adafruit_tca9548a.PCA9546A(i2c)

# For each sensor, create it using the PCA9546A channel instead of the I2C object
tsl1 = adafruit_tsl2591.TSL2591(mux[0])
tsl2 = adafruit_tsl2591.TSL2591(mux[1])

# After initial setup, can just use sensors as normal.
while True:
    print(tsl1.lux, tsl2.lux)
    time.sleep(0.1)
