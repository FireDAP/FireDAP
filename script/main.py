import time
time.sleep(2)
import machine
import uasyncio as asyncio
import lvgl as lv
from hal.st7789 import *
from gui.async_utils import Lv_Async
from gui_driver import Display_Driver
from script.firedap_ui import FireDAP_UI
from ili9xxx import *
from st77xx import St7735,ST77XX_PORTRAIT

import gc
gc.collect()
gc.threshold( gc.mem_free() // 4 + gc.mem_alloc() )


lcd_baudrate = 24_000_000
tsc_baudrate = 1_000_000
adc_frequency = 10_000_000
pwm_frequency = 1_000_000

spi_sck = machine.Pin( 10, machine.Pin.OUT )
spi_mosi= machine.Pin( 11, machine.Pin.OUT )
spi_miso= machine.Pin( 12, machine.Pin.IN  )
spi_dc  = machine.Pin( 8, machine.Pin.OUT )

lcd_rst = machine.Pin( 15, machine.Pin.OUT )
lcd_bl  = machine.Pin( 13, machine.Pin.OUT )
lcd_cs  = machine.Pin( 9, machine.Pin.OUT )



# Calibration values
print( "tsc()" )
tsc = None


# Init lcd last one to start lvgl with SPI LCD baudrate
print( "lcd()" )
# lcd = St7735(
#     mhz=3, mosi=11, clk=10, cs=9, dc=8, rst=15, power=-15, backlight=13, backlight_on=13)

lcd = St7789( lcd_baudrate, lcd_cs, spi_sck, spi_mosi, spi_miso, spi_dc, lcd_rst, lcd_bl )
#  w, h = 160//4, 80//4
#  bmp = build_square_buf( w, h )
#
#  t0 = time.ticks_us()
#  lcd.draw_bitmap_dma( 30, 60, w, h, bmp )
#  t1 = time.ticks_us()
#
#  print( "Maximum FPS @24MHz:", 24e6/( 160*80*16 ) ) # FPS = F/(W*H*BPP)
#  print( "Achieved FPS:", 1/(16*(t1-t0)*1e-6) )       # Note: Test only draws 1/16 of the sreen area
#
#  print( "Draw TSC calibration pattern")
#  w, h = 100, 100
#  bmp = build_square_buf( w, h )
lv.deinit()
display_driver = Display_Driver( 160, 80, lcd, tsc )

try:
    scr = lv.scr_act()
    scr_style = lv.style_t()
    scr_style.set_bg_color(lv.color_hex(0x003a00))
    scr.add_style(scr_style,0)

    label = lv.label(lv.scr_act())
    label_style = lv.style_t()
    label_style.set_text_color(lv.color_hex(0xffffff))
    label.set_text("Hello world")
    label.add_style(label_style,0)
    label.align(lv.ALIGN.CENTER, 0, 0)

    lv.scr_load(scr)

    print( "run" )
    lva = Lv_Async(refresh_rate=20 )
    asyncio.Loop.run_forever()

except Exception as error:
    print(error)
    lv.deinit()


