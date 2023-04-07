###############################################################
# SSD1306 OLED Display I2C Tests with the Raspberry Pi Pico
# with MicroPython on the Raspberry Pi 4
#
# by Joshua Hrisko, Maker Portal LLC (c) 2021
#
#
# Based on the Pico Micropython repository at:
# https://github.com/raspberrypi/pico-micropython-examples/tree/master/i2c/1306oled
###############################################################
#
#
from machine import Pin, I2C, SPI
import sys,gc

ssd1306_pix_res_x  = 128 # SSD1306 horizontal resolution
ssd1306_pix_res_y = 64   # SSD1306 vertical resolution

st7735_pix_res_x = 80
st7735_pix_res_y = 160

i2c_dev = I2C(1,scl=Pin(27),sda=Pin(26),freq=200000)  # start I2C on I2C1 (GPIO 26/27)
i2c_addr = [hex(ii) for ii in i2c_dev.scan()] # get I2C address in hex format

global ssd 

if i2c_addr==[]:
    print('No I2C Display Found') 
    from drivers.st7735r.st7735r import ST7735R as SSD
    pdc = Pin(18, Pin.OUT, value=0)  # Arbitrary pins
    pcs = Pin(19, Pin.OUT, value=1)
    prst = Pin(20, Pin.OUT, value=1)
    spi_dev = SPI(0, baudrate=80_000_000, polarity=0, phase=0, bits=8, sck=Pin(6), mosi=Pin(7), miso=Pin(4))

    gc.collect()
    ssd = SSD(spi_dev, pcs, pdc, prst)  # The other Adafruit displays use defaults

else:
    print("I2C Address      : {}".format(i2c_addr[0])) # I2C device address
    print("I2C Configuration: {}".format(i2c_dev)) # print I2C params
    from drivers.ssd1306.ssd1306 import SSD1306_I2C as SSD

    gc.collect()
    ssd = SSD(ssd1306_pix_res_x, ssd1306_pix_res_y, i2c_dev) # oled controller



from gui.core.ugui import Display
nxt = Pin(21, Pin.IN, Pin.PULL_UP)  # Move to next control
sel = Pin(22, Pin.IN, Pin.PULL_UP)  # Operate current control
display = Display(ssd, nxt, sel)  # Encoder mode

