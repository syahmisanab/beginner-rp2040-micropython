
# Wizbot Robot OLED Display Installation Guide

This guide provides step-by-step instructions for installing an OLED display on the Wizbot robot. We will be using a Raspberry Pi with the OLED display, leveraging the I2C communication protocol.

## Prerequisites

- Raspberry Pi (with Ubuntu 18.04 or a similar OS)
- OLED display (compatible with the SSD1306 driver)
- Internet connection on Raspberry Pi
- Basic familiarity with terminal commands

## Installation Steps

### Step 1: Enable I2C on Raspberry Pi

The I2C interface on the Raspberry Pi needs to be enabled to communicate with the OLED display. Follow these steps:

1. **Install I2C tools and SMBus**:
   ```bash
   sudo apt install i2c-tools python-smbus
   ```

2. **Enable I2C Interface**:
   Open the Raspberry Pi configuration file:
   ```bash
   sudo nano /boot/firmware/usercfg.txt
   ```
   Add the following line to enable the I2C interface:
   ```text
   dtparam=i2c_arm=on
   ```
   Save and exit the file (CTRL+X, then Y, then Enter).

3. **Install GPIO Library**:
   ```bash
   sudo apt install rpi.gpio
   ```

4. **Check if I2C is Available**:
   Use the following command to verify if I2C devices are detected:
   ```bash
   sudo i2cdetect -y 1
   ```
   Note down the address of the detected devices.

### Step 2: Install OLED Library

We'll use the Adafruit SSD1306 Python library for the OLED display.

1. **Clone the Adafruit SSD1306 Repository**:
   ```bash
   git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
   ```

2. **Navigate to the Repository Directory**:
   ```bash
   cd Adafruit_Python_SSD1306
   ```

3. **Install the Library**:
   ```bash
   sudo python3 setup.py install
   ```

### Step 3: Test the Display

Run the provided example script to test if the OLED display is working correctly.

1. **Navigate to the Examples Directory**:
   ```bash
   cd examples
   ```

2. **Run the Test Script**:
   ```bash
   python3 stats.py
   ```

   This script should display system statistics on the OLED screen. If the display is working correctly, you should see text and graphics on the screen.

## Troubleshooting

If you encounter any issues, please ensure all connections are secure and the I2C address matches the address in your script. For further assistance, raise an issue in this repository.

## Contributions

Contributions to this guide are welcome. Please fork the repository and submit a pull request with your improvements.

## License

[Add your chosen license here]

