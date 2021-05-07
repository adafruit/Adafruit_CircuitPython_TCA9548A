# SPDX-FileCopyrightText: 2021 codenio (Aananth K)
# SPDX-License-Identifier: MIT

# This example shows scanning of each TCA9548A channels.
import board
import busio
import adafruit_tca9548a

# Create I2C bus as normal
i2c = busio.I2C(board.SCL, board.SDA)

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# Scan the Main I2C Channel present in your board
print("Scan of Main I2C Channel:{}".format([hex(i) for i in i2c.scan()]))

# Scan Each TCA9548A channel
for i in range(8):
    print("Scan of TCA[{}] Channel: {}".format(i, [hex(j) for j in tca[i].scan()]))
