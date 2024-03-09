import usys as sys
import lvgl as lv
import fs_driver
import lv_utils
from  lv_utils import event_loop



class hal:
    def __init__(self):
        self.group = lv.group_create()
        self.group.set_default()

        if not event_loop.is_running():
            if sys.platform == 'rp2':
                self.init_rp2_gui()
            elif sys.platform == 'linux':
                self.init_sdl_gui()

    def init_sdl_gui(self):
        self.event_loop = lv_utils.event_loop()
        self.disp_drv = lv.sdl_window_create(240, 280)
        self.indev_drv = lv.sdl_mouse_create()
        self.keyboard = lv.sdl_keyboard_create()
        self.keyboard.set_group(self.group)

        ## fs driver init
        self.fs_drv = lv.fs_drv_t()
        fs_driver.fs_register(self.fs_drv, 'S')


    def init_rp2_gui(self):
        import st77xx
        spi=machine.SPI(
            1,
            baudrate=24_000_000,
            polarity=0,
            phase=0,
            sck=machine.Pin(10,machine.Pin.OUT),
            mosi=machine.Pin(11,machine.Pin.OUT),
            miso=machine.Pin(12,machine.Pin.IN)
        )
        self.disp=st77xx.St7789(rot=st77xx.ST77XX_INV_LANDSCAPE,res=(240,280),spi=spi,cs=9,dc=8,bl=13,rst=15,rp2_dma=None)
        self.disp.set_backlight(100)


