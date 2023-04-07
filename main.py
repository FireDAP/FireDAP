import hardware_setup   # Create a display instance
from gui.core.ugui import Screen, ssd
from gui.core.colors import *
from gui.core.writer import CWriter,Writer
import gui.fonts.arial10 as arial10
import gui.fonts.freesans20 as freesans20
from gui.widgets import Label,CloseButton

global wri


class BaseScreen(Screen):
    def __init__(self):
        super().__init__()
        if str(ssd).find('SSD1306_I2C') == 1 :
            print("find ssd1306 device")
            wri = Writer(ssd, arial10)
        elif str(ssd).find('ST7735R') == 1 :
            print("find st7735r device")
            wri = CWriter(ssd, arial10, GREEN , BLACK)

        Label(wri, 2, 2, 'KiwiDAP Menu')
                

        
def main():
        Screen.change(BaseScreen)

main()